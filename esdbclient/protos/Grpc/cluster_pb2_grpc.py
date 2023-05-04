# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from esdbclient.protos.Grpc import (
    cluster_pb2 as esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2,
    shared_pb2 as esdbclient_dot_protos_dot_Grpc_dot_shared__pb2,
)


class GossipStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Update = channel.unary_unary(
            "/event_store.cluster.Gossip/Update",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.GossipRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.FromString,
        )
        self.Read = channel.unary_unary(
            "/event_store.cluster.Gossip/Read",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.FromString,
        )


class GossipServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GossipServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.GossipRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.SerializeToString,
        ),
        "Read": grpc.unary_unary_rpc_method_handler(
            servicer.Read,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "event_store.cluster.Gossip", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Gossip(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Gossip/Update",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.GossipRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Read(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Gossip/Read",
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ClusterInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class ElectionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ViewChange = channel.unary_unary(
            "/event_store.cluster.Elections/ViewChange",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.ViewChangeProof = channel.unary_unary(
            "/event_store.cluster.Elections/ViewChangeProof",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeProofRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.Prepare = channel.unary_unary(
            "/event_store.cluster.Elections/Prepare",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.PrepareOk = channel.unary_unary(
            "/event_store.cluster.Elections/PrepareOk",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareOkRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.Proposal = channel.unary_unary(
            "/event_store.cluster.Elections/Proposal",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ProposalRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.Accept = channel.unary_unary(
            "/event_store.cluster.Elections/Accept",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.AcceptRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.LeaderIsResigning = channel.unary_unary(
            "/event_store.cluster.Elections/LeaderIsResigning",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )
        self.LeaderIsResigningOk = channel.unary_unary(
            "/event_store.cluster.Elections/LeaderIsResigningOk",
            request_serializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningOkRequest.SerializeToString,
            response_deserializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
        )


class ElectionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ViewChange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ViewChangeProof(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Prepare(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PrepareOk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Proposal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Accept(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LeaderIsResigning(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def LeaderIsResigningOk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ElectionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ViewChange": grpc.unary_unary_rpc_method_handler(
            servicer.ViewChange,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "ViewChangeProof": grpc.unary_unary_rpc_method_handler(
            servicer.ViewChangeProof,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeProofRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "Prepare": grpc.unary_unary_rpc_method_handler(
            servicer.Prepare,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "PrepareOk": grpc.unary_unary_rpc_method_handler(
            servicer.PrepareOk,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareOkRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "Proposal": grpc.unary_unary_rpc_method_handler(
            servicer.Proposal,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ProposalRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "Accept": grpc.unary_unary_rpc_method_handler(
            servicer.Accept,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.AcceptRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "LeaderIsResigning": grpc.unary_unary_rpc_method_handler(
            servicer.LeaderIsResigning,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
        "LeaderIsResigningOk": grpc.unary_unary_rpc_method_handler(
            servicer.LeaderIsResigningOk,
            request_deserializer=esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningOkRequest.FromString,
            response_serializer=esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "event_store.cluster.Elections", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Elections(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ViewChange(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/ViewChange",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ViewChangeProof(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/ViewChangeProof",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ViewChangeProofRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Prepare(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/Prepare",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PrepareOk(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/PrepareOk",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.PrepareOkRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Proposal(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/Proposal",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.ProposalRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Accept(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/Accept",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.AcceptRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LeaderIsResigning(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/LeaderIsResigning",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LeaderIsResigningOk(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/event_store.cluster.Elections/LeaderIsResigningOk",
            esdbclient_dot_protos_dot_Grpc_dot_cluster__pb2.LeaderIsResigningOkRequest.SerializeToString,
            esdbclient_dot_protos_dot_Grpc_dot_shared__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )