# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional, Sequence

from grpc import CallCredentials, Channel, RpcError

from esdbclient.esdbapibase import ESDBService, Metadata, handle_rpc_error
from esdbclient.protos.Grpc import (
    cluster_pb2,
    cluster_pb2_grpc,
    gossip_pb2,
    gossip_pb2_grpc,
    shared_pb2,
)


@dataclass
class ClusterMember:
    state: str
    address: str
    port: int


NODE_STATE_LEADER = "NODE_STATE_LEADER"
NODE_STATE_FOLLOWER = "NODE_STATE_FOLLOWER"
NODE_STATE_REPLICA = "NODE_STATE_REPLICA"
NODE_STATE_OTHER = "NODE_STATE_OTHER"
GOSSIP_API_NODE_STATES_MAPPING = {
    gossip_pb2.MemberInfo.VNodeState.Follower: NODE_STATE_FOLLOWER,
    gossip_pb2.MemberInfo.VNodeState.Leader: NODE_STATE_LEADER,
    gossip_pb2.MemberInfo.VNodeState.ReadOnlyReplica: NODE_STATE_REPLICA,
}


class BaseGossipService:
    def __init__(self, channel: Channel):
        self._stub = gossip_pb2_grpc.GossipStub(channel)

    def _construct_cluster_members(
        self, cluster_info: gossip_pb2.ClusterInfo
    ) -> Sequence[ClusterMember]:
        members = []
        for member_info in cluster_info.members:
            member = ClusterMember(
                GOSSIP_API_NODE_STATES_MAPPING.get(member_info.state, NODE_STATE_OTHER),
                member_info.http_end_point.address,
                member_info.http_end_point.port,
            )
            members.append(member)
        return tuple(members)


class GossipService(ESDBService, BaseGossipService):
    """
    Encapsulates the 'gossip.Gossip' gRPC service.
    """

    def read(
        self,
        timeout: Optional[float] = None,
        metadata: Optional[Metadata] = None,
        credentials: Optional[CallCredentials] = None,
    ) -> Sequence[ClusterMember]:
        try:
            read_resp = self._stub.Read(
                shared_pb2.Empty(),
                timeout=timeout,
                metadata=self._metadata(metadata),
                credentials=credentials,
            )
        except RpcError as e:
            raise handle_rpc_error(e) from e

        return self._construct_cluster_members(read_resp)


CLUSTER_GOSSIP_NODE_STATES_MAPPING = {
    cluster_pb2.MemberInfo.VNodeState.Follower: NODE_STATE_FOLLOWER,
    cluster_pb2.MemberInfo.VNodeState.Leader: NODE_STATE_LEADER,
    cluster_pb2.MemberInfo.VNodeState.ReadOnlyReplica: NODE_STATE_REPLICA,
}


class ClusterGossipService(ESDBService):
    """
    Encapsulates the 'cluster.Gossip' gRPC service.
    """

    def __init__(self, channel: Channel):
        self._stub = cluster_pb2_grpc.GossipStub(channel)

    def read(
        self,
        timeout: Optional[float] = None,
        metadata: Optional[Metadata] = None,
        credentials: Optional[CallCredentials] = None,
    ) -> Sequence[ClusterMember]:
        """
        Returns a sequence of ClusterMember
        """

        try:
            read_resp = self._stub.Read(
                shared_pb2.Empty(),
                timeout=timeout,
                metadata=self._metadata(metadata),
                credentials=credentials,
            )
        except RpcError as e:
            raise handle_rpc_error(e) from e

        assert isinstance(read_resp, cluster_pb2.ClusterInfo)

        members = []
        for member_info in read_resp.members:
            assert isinstance(member_info, cluster_pb2.MemberInfo)
            # Todo: Here we might want to use member_info.advertise_host_to_client_as
            #   and member_info.advertise_http_port_to_client_as, but I don't know
            #   what the difference is. Are these different from
            #   member_info.http_end_point.address and member_info.http_end_point.port?
            member = ClusterMember(
                state=CLUSTER_GOSSIP_NODE_STATES_MAPPING.get(
                    member_info.state, NODE_STATE_OTHER
                ),
                address=member_info.http_end_point.address,
                port=member_info.http_end_point.port,
            )
            members.append(member)
        return tuple(members)
