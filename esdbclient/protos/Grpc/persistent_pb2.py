# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: esdbclient/protos/Grpc/persistent.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from esdbclient.protos.Grpc import (
    shared_pb2 as esdbclient_dot_protos_dot_Grpc_dot_shared__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n'esdbclient/protos/Grpc/persistent.proto\x12+event_store.client.persistent_subscriptions\x1a#esdbclient/protos/Grpc/shared.proto\"\x99\x07\n\x07ReadReq\x12O\n\x07options\x18\x01"
    b" \x01(\x0b\x32<.event_store.client.persistent_subscriptions.ReadReq.OptionsH\x00\x12G\n\x03\x61\x63k\x18\x02"
    b" \x01(\x0b\x32\x38.event_store.client.persistent_subscriptions.ReadReq.AckH\x00\x12I\n\x04nack\x18\x03"
    b" \x01(\x0b\x32\x39.event_store.client.persistent_subscriptions.ReadReq.NackH\x00\x1a\x85\x03\n\x07Options\x12\x41\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierH\x00\x12(\n\x03\x61ll\x18\x05"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x12\n\ngroup_name\x18\x02"
    b" \x01(\t\x12\x13\n\x0b\x62uffer_size\x18\x03"
    b" \x01(\x05\x12\\\n\x0buuid_option\x18\x04"
    b" \x01(\x0b\x32G.event_store.client.persistent_subscriptions.ReadReq.Options.UUIDOption\x1au\n\nUUIDOption\x12/\n\nstructured\x18\x01"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12+\n\x06string\x18\x02"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\t\n\x07\x63ontentB\x0f\n\rstream_option\x1a\x38\n\x03\x41\x63k\x12\n\n\x02id\x18\x01"
    b" \x01(\x0c\x12%\n\x03ids\x18\x02"
    b" \x03(\x0b\x32\x18.event_store.client.UUID\x1a\xdb\x01\n\x04Nack\x12\n\n\x02id\x18\x01"
    b" \x01(\x0c\x12%\n\x03ids\x18\x02"
    b" \x03(\x0b\x32\x18.event_store.client.UUID\x12P\n\x06\x61\x63tion\x18\x03"
    b" \x01(\x0e\x32@.event_store.client.persistent_subscriptions.ReadReq.Nack.Action\x12\x0e\n\x06reason\x18\x04"
    b' \x01(\t">\n\x06\x41\x63tion\x12\x0b\n\x07Unknown\x10\x00\x12\x08\n\x04Park\x10\x01\x12\t\n\x05Retry\x10\x02\x12\x08\n\x04Skip\x10\x03\x12\x08\n\x04Stop\x10\x04\x42\t\n\x07\x63ontent"\x94\x08\n\x08ReadResp\x12P\n\x05\x65vent\x18\x01'
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.ReadResp.ReadEventH\x00\x12s\n\x19subscription_confirmation\x18\x02"
    b" \x01(\x0b\x32N.event_store.client.persistent_subscriptions.ReadResp.SubscriptionConfirmationH\x00\x1a\x80\x06\n\tReadEvent\x12\\\n\x05\x65vent\x18\x01"
    b" \x01(\x0b\x32M.event_store.client.persistent_subscriptions.ReadResp.ReadEvent.RecordedEvent\x12[\n\x04link\x18\x02"
    b" \x01(\x0b\x32M.event_store.client.persistent_subscriptions.ReadResp.ReadEvent.RecordedEvent\x12\x19\n\x0f\x63ommit_position\x18\x03"
    b" \x01(\x04H\x00\x12\x30\n\x0bno_position\x18\x04"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x15\n\x0bretry_count\x18\x05"
    b" \x01(\x05H\x01\x12\x33\n\x0eno_retry_count\x18\x06"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x01\x1a\x89\x03\n\rRecordedEvent\x12$\n\x02id\x18\x01"
    b" \x01(\x0b\x32\x18.event_store.client.UUID\x12?\n\x11stream_identifier\x18\x02"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifier\x12\x17\n\x0fstream_revision\x18\x03"
    b" \x01(\x04\x12\x18\n\x10prepare_position\x18\x04"
    b" \x01(\x04\x12\x17\n\x0f\x63ommit_position\x18\x05"
    b" \x01(\x04\x12m\n\x08metadata\x18\x06"
    b" \x03(\x0b\x32[.event_store.client.persistent_subscriptions.ReadResp.ReadEvent.RecordedEvent.MetadataEntry\x12\x17\n\x0f\x63ustom_metadata\x18\x07"
    b" \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x08"
    b" \x01(\x0c\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\r\n\x05value\x18\x02"
    b" \x01(\t:\x02\x38\x01\x42\n\n\x08positionB\x07\n\x05\x63ount\x1a\x33\n\x18SubscriptionConfirmation\x12\x17\n\x0fsubscription_id\x18\x01"
    b' \x01(\tB\t\n\x07\x63ontent"\xf6\x10\n\tCreateReq\x12O\n\x07options\x18\x01'
    b" \x01(\x0b\x32>.event_store.client.persistent_subscriptions.CreateReq.Options\x1a\xf0\x02\n\x07Options\x12V\n\x06stream\x18\x04"
    b" \x01(\x0b\x32\x44.event_store.client.persistent_subscriptions.CreateReq.StreamOptionsH\x00\x12P\n\x03\x61ll\x18\x05"
    b" \x01(\x0b\x32\x41.event_store.client.persistent_subscriptions.CreateReq.AllOptionsH\x00\x12\x43\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierB\x02\x18\x01\x12\x12\n\ngroup_name\x18\x02"
    b" \x01(\t\x12Q\n\x08settings\x18\x03"
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.CreateReq.SettingsB\x0f\n\rstream_option\x1a\xcd\x01\n\rStreamOptions\x12?\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifier\x12\x12\n\x08revision\x18\x02"
    b" \x01(\x04H\x00\x12*\n\x05start\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12(\n\x03\x65nd\x18\x04"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\x11\n\x0frevision_option\x1a\x88\x06\n\nAllOptions\x12S\n\x08position\x18\x01"
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.CreateReq.PositionH\x00\x12*\n\x05start\x18\x02"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12(\n\x03\x65nd\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x61\n\x06\x66ilter\x18\x04"
    b" \x01(\x0b\x32O.event_store.client.persistent_subscriptions.CreateReq.AllOptions.FilterOptionsH\x01\x12.\n\tno_filter\x18\x05"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x01\x1a\x9c\x03\n\rFilterOptions\x12w\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32Z.event_store.client.persistent_subscriptions.CreateReq.AllOptions.FilterOptions.ExpressionH\x00\x12p\n\nevent_type\x18\x02"
    b" \x01(\x0b\x32Z.event_store.client.persistent_subscriptions.CreateReq.AllOptions.FilterOptions.ExpressionH\x00\x12\r\n\x03max\x18\x03"
    b" \x01(\rH\x01\x12*\n\x05\x63ount\x18\x04"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x01\x12$\n\x1c\x63heckpointIntervalMultiplier\x18\x05"
    b" \x01(\r\x1a+\n\nExpression\x12\r\n\x05regex\x18\x01"
    b" \x01(\t\x12\x0e\n\x06prefix\x18\x02"
    b" \x03(\tB\x08\n\x06\x66ilterB\x08\n\x06windowB\x0c\n\nall_optionB\x0f\n\rfilter_option\x1a=\n\x08Position\x12\x17\n\x0f\x63ommit_position\x18\x01"
    b" \x01(\x04\x12\x18\n\x10prepare_position\x18\x02"
    b" \x01(\x04\x1a\xc4\x04\n\x08Settings\x12\x15\n\rresolve_links\x18\x01"
    b" \x01(\x08\x12\x14\n\x08revision\x18\x02"
    b" \x01(\x04\x42\x02\x18\x01\x12\x18\n\x10\x65xtra_statistics\x18\x03"
    b" \x01(\x08\x12\x17\n\x0fmax_retry_count\x18\x05"
    b" \x01(\x05\x12\x1c\n\x14min_checkpoint_count\x18\x07"
    b" \x01(\x05\x12\x1c\n\x14max_checkpoint_count\x18\x08"
    b" \x01(\x05\x12\x1c\n\x14max_subscriber_count\x18\t"
    b" \x01(\x05\x12\x18\n\x10live_buffer_size\x18\n"
    b" \x01(\x05\x12\x17\n\x0fread_batch_size\x18\x0b"
    b" \x01(\x05\x12\x1b\n\x13history_buffer_size\x18\x0c"
    b" \x01(\x05\x12l\n\x17named_consumer_strategy\x18\r"
    b" \x01(\x0e\x32G.event_store.client.persistent_subscriptions.CreateReq.ConsumerStrategyB\x02\x18\x01\x12\x1f\n\x15message_timeout_ticks\x18\x04"
    b" \x01(\x03H\x00\x12\x1c\n\x12message_timeout_ms\x18\x0e \x01(\x05H\x00\x12"
    b" \n\x16\x63heckpoint_after_ticks\x18\x06"
    b" \x01(\x03H\x01\x12\x1d\n\x13\x63heckpoint_after_ms\x18\x0f"
    b" \x01(\x05H\x01\x12\x19\n\x11\x63onsumer_strategy\x18\x10"
    b' \x01(\tB\x11\n\x0fmessage_timeoutB\x12\n\x10\x63heckpoint_after"D\n\x10\x43onsumerStrategy\x12\x14\n\x10\x44ispatchToSingle\x10\x00\x12\x0e\n\nRoundRobin\x10\x01\x12\n\n\x06Pinned\x10\x02"\x0c\n\nCreateResp"\x94\x0c\n\tUpdateReq\x12O\n\x07options\x18\x01'
    b" \x01(\x0b\x32>.event_store.client.persistent_subscriptions.UpdateReq.Options\x1a\xf0\x02\n\x07Options\x12V\n\x06stream\x18\x04"
    b" \x01(\x0b\x32\x44.event_store.client.persistent_subscriptions.UpdateReq.StreamOptionsH\x00\x12P\n\x03\x61ll\x18\x05"
    b" \x01(\x0b\x32\x41.event_store.client.persistent_subscriptions.UpdateReq.AllOptionsH\x00\x12\x43\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierB\x02\x18\x01\x12\x12\n\ngroup_name\x18\x02"
    b" \x01(\t\x12Q\n\x08settings\x18\x03"
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.UpdateReq.SettingsB\x0f\n\rstream_option\x1a\xcd\x01\n\rStreamOptions\x12?\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifier\x12\x12\n\x08revision\x18\x02"
    b" \x01(\x04H\x00\x12*\n\x05start\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12(\n\x03\x65nd\x18\x04"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\x11\n\x0frevision_option\x1a\xc5\x01\n\nAllOptions\x12S\n\x08position\x18\x01"
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.UpdateReq.PositionH\x00\x12*\n\x05start\x18\x02"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12(\n\x03\x65nd\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\x0c\n\nall_option\x1a=\n\x08Position\x12\x17\n\x0f\x63ommit_position\x18\x01"
    b" \x01(\x04\x12\x18\n\x10prepare_position\x18\x02"
    b" \x01(\x04\x1a\xa5\x04\n\x08Settings\x12\x15\n\rresolve_links\x18\x01"
    b" \x01(\x08\x12\x14\n\x08revision\x18\x02"
    b" \x01(\x04\x42\x02\x18\x01\x12\x18\n\x10\x65xtra_statistics\x18\x03"
    b" \x01(\x08\x12\x17\n\x0fmax_retry_count\x18\x05"
    b" \x01(\x05\x12\x1c\n\x14min_checkpoint_count\x18\x07"
    b" \x01(\x05\x12\x1c\n\x14max_checkpoint_count\x18\x08"
    b" \x01(\x05\x12\x1c\n\x14max_subscriber_count\x18\t"
    b" \x01(\x05\x12\x18\n\x10live_buffer_size\x18\n"
    b" \x01(\x05\x12\x17\n\x0fread_batch_size\x18\x0b"
    b" \x01(\x05\x12\x1b\n\x13history_buffer_size\x18\x0c"
    b" \x01(\x05\x12h\n\x17named_consumer_strategy\x18\r"
    b" \x01(\x0e\x32G.event_store.client.persistent_subscriptions.UpdateReq.ConsumerStrategy\x12\x1f\n\x15message_timeout_ticks\x18\x04"
    b" \x01(\x03H\x00\x12\x1c\n\x12message_timeout_ms\x18\x0e \x01(\x05H\x00\x12"
    b" \n\x16\x63heckpoint_after_ticks\x18\x06"
    b" \x01(\x03H\x01\x12\x1d\n\x13\x63heckpoint_after_ms\x18\x0f"
    b' \x01(\x05H\x01\x42\x11\n\x0fmessage_timeoutB\x12\n\x10\x63heckpoint_after"D\n\x10\x43onsumerStrategy\x12\x14\n\x10\x44ispatchToSingle\x10\x00\x12\x0e\n\nRoundRobin\x10\x01\x12\n\n\x06Pinned\x10\x02"\x0c\n\nUpdateResp"\xfa\x01\n\tDeleteReq\x12O\n\x07options\x18\x01'
    b" \x01(\x0b\x32>.event_store.client.persistent_subscriptions.DeleteReq.Options\x1a\x9b\x01\n\x07Options\x12\x41\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierH\x00\x12(\n\x03\x61ll\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x12\n\ngroup_name\x18\x02"
    b' \x01(\tB\x0f\n\rstream_option"\x0c\n\nDeleteResp"\xfc\x01\n\nGetInfoReq\x12P\n\x07options\x18\x01'
    b" \x01(\x0b\x32?.event_store.client.persistent_subscriptions.GetInfoReq.Options\x1a\x9b\x01\n\x07Options\x12\x41\n\x11stream_identifier\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierH\x00\x12(\n\x03\x61ll\x18\x02"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x12\n\ngroup_name\x18\x03"
    b' \x01(\tB\x0f\n\rstream_option"g\n\x0bGetInfoResp\x12X\n\x11subscription_info\x18\x01'
    b' \x01(\x0b\x32=.event_store.client.persistent_subscriptions.SubscriptionInfo"\xf0\t\n\x10SubscriptionInfo\x12\x14\n\x0c\x65vent_source\x18\x01'
    b" \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03"
    b" \x01(\t\x12\x61\n\x0b\x63onnections\x18\x04"
    b" \x03(\x0b\x32L.event_store.client.persistent_subscriptions.SubscriptionInfo.ConnectionInfo\x12\x1a\n\x12\x61verage_per_second\x18\x05"
    b" \x01(\x05\x12\x13\n\x0btotal_items\x18\x06"
    b" \x01(\x03\x12$\n\x1c\x63ount_since_last_measurement\x18\x07 \x01(\x03\x12(\n"
    b" last_checkpointed_event_position\x18\x08"
    b" \x01(\t\x12!\n\x19last_known_event_position\x18\t"
    b" \x01(\t\x12\x18\n\x10resolve_link_tos\x18\n"
    b" \x01(\x08\x12\x12\n\nstart_from\x18\x0b"
    b" \x01(\t\x12$\n\x1cmessage_timeout_milliseconds\x18\x0c"
    b" \x01(\x05\x12\x18\n\x10\x65xtra_statistics\x18\r"
    b" \x01(\x08\x12\x17\n\x0fmax_retry_count\x18\x0e"
    b" \x01(\x05\x12\x18\n\x10live_buffer_size\x18\x0f"
    b" \x01(\x05\x12\x13\n\x0b\x62uffer_size\x18\x10"
    b" \x01(\x05\x12\x17\n\x0fread_batch_size\x18\x11"
    b" \x01(\x05\x12&\n\x1e\x63heck_point_after_milliseconds\x18\x12"
    b" \x01(\x05\x12\x1d\n\x15min_check_point_count\x18\x13"
    b" \x01(\x05\x12\x1d\n\x15max_check_point_count\x18\x14"
    b" \x01(\x05\x12\x19\n\x11read_buffer_count\x18\x15"
    b" \x01(\x05\x12\x19\n\x11live_buffer_count\x18\x16"
    b" \x01(\x03\x12\x1a\n\x12retry_buffer_count\x18\x17 \x01(\x05\x12"
    b" \n\x18total_in_flight_messages\x18\x18"
    b' \x01(\x05\x12"\n\x1aoutstanding_messages_count\x18\x19'
    b" \x01(\x05\x12\x1f\n\x17named_consumer_strategy\x18\x1a"
    b" \x01(\t\x12\x1c\n\x14max_subscriber_count\x18\x1b"
    b" \x01(\x05\x12\x1c\n\x14parked_message_count\x18\x1c"
    b" \x01(\x03\x1a\xc5\x02\n\x0e\x43onnectionInfo\x12\x0c\n\x04\x66rom\x18\x01"
    b" \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12"
    b" \n\x18\x61verage_items_per_second\x18\x03"
    b" \x01(\x05\x12\x13\n\x0btotal_items\x18\x04"
    b" \x01(\x03\x12$\n\x1c\x63ount_since_last_measurement\x18\x05"
    b" \x01(\x03\x12h\n\x15observed_measurements\x18\x06"
    b" \x03(\x0b\x32I.event_store.client.persistent_subscriptions.SubscriptionInfo.Measurement\x12\x17\n\x0f\x61vailable_slots\x18\x07"
    b" \x01(\x05\x12\x1a\n\x12in_flight_messages\x18\x08"
    b" \x01(\x05\x12\x17\n\x0f\x63onnection_name\x18\t"
    b" \x01(\t\x1a)\n\x0bMeasurement\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\r\n\x05value\x18\x02"
    b' \x01(\x03"\xda\x02\n\x0fReplayParkedReq\x12U\n\x07options\x18\x01'
    b" \x01(\x0b\x32\x44.event_store.client.persistent_subscriptions.ReplayParkedReq.Options\x1a\xef\x01\n\x07Options\x12\x12\n\ngroup_name\x18\x01"
    b" \x01(\t\x12\x41\n\x11stream_identifier\x18\x02"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierH\x00\x12(\n\x03\x61ll\x18\x03"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\x11\n\x07stop_at\x18\x04"
    b" \x01(\x03H\x01\x12-\n\x08no_limit\x18\x05"
    b' \x01(\x0b\x32\x19.event_store.client.EmptyH\x01\x42\x0f\n\rstream_optionB\x10\n\x0estop_at_option"\x12\n\x10ReplayParkedResp"\x92\x03\n\x07ListReq\x12M\n\x07options\x18\x01'
    b" \x01(\x0b\x32<.event_store.client.persistent_subscriptions.ListReq.Options\x1a\xb3\x01\n\x07Options\x12;\n\x16list_all_subscriptions\x18\x01"
    b" \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x12\\\n\x0flist_for_stream\x18\x02"
    b" \x01(\x0b\x32\x41.event_store.client.persistent_subscriptions.ListReq.StreamOptionH\x00\x42\r\n\x0blist_option\x1a\x81\x01\n\x0cStreamOption\x12\x36\n\x06stream\x18\x01"
    b" \x01(\x0b\x32$.event_store.client.StreamIdentifierH\x00\x12(\n\x03\x61ll\x18\x02"
    b' \x01(\x0b\x32\x19.event_store.client.EmptyH\x00\x42\x0f\n\rstream_option"`\n\x08ListResp\x12T\n\rsubscriptions\x18\x01'
    b" \x03(\x0b\x32=.event_store.client.persistent_subscriptions.SubscriptionInfo2\xce\x07\n\x17PersistentSubscriptions\x12y\n\x06\x43reate\x12\x36.event_store.client.persistent_subscriptions.CreateReq\x1a\x37.event_store.client.persistent_subscriptions.CreateResp\x12y\n\x06Update\x12\x36.event_store.client.persistent_subscriptions.UpdateReq\x1a\x37.event_store.client.persistent_subscriptions.UpdateResp\x12y\n\x06\x44\x65lete\x12\x36.event_store.client.persistent_subscriptions.DeleteReq\x1a\x37.event_store.client.persistent_subscriptions.DeleteResp\x12w\n\x04Read\x12\x34.event_store.client.persistent_subscriptions.ReadReq\x1a\x35.event_store.client.persistent_subscriptions.ReadResp(\x01\x30\x01\x12|\n\x07GetInfo\x12\x37.event_store.client.persistent_subscriptions.GetInfoReq\x1a\x38.event_store.client.persistent_subscriptions.GetInfoResp\x12\x8b\x01\n\x0cReplayParked\x12<.event_store.client.persistent_subscriptions.ReplayParkedReq\x1a=.event_store.client.persistent_subscriptions.ReplayParkedResp\x12s\n\x04List\x12\x34.event_store.client.persistent_subscriptions.ListReq\x1a\x35.event_store.client.persistent_subscriptions.ListResp\x12H\n\x10RestartSubsystem\x12\x19.event_store.client.Empty\x1a\x19.event_store.client.EmptyB7\n5com.eventstore.dbclient.proto.persistentsubscriptionsb\x06proto3"
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "esdbclient.protos.Grpc.persistent_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n5com.eventstore.dbclient.proto.persistentsubscriptions"
    )
    _READRESP_READEVENT_RECORDEDEVENT_METADATAENTRY._options = None
    _READRESP_READEVENT_RECORDEDEVENT_METADATAENTRY._serialized_options = b"8\001"
    _CREATEREQ_OPTIONS.fields_by_name["stream_identifier"]._options = None
    _CREATEREQ_OPTIONS.fields_by_name["stream_identifier"]._serialized_options = (
        b"\030\001"
    )
    _CREATEREQ_SETTINGS.fields_by_name["revision"]._options = None
    _CREATEREQ_SETTINGS.fields_by_name["revision"]._serialized_options = b"\030\001"
    _CREATEREQ_SETTINGS.fields_by_name["named_consumer_strategy"]._options = None
    _CREATEREQ_SETTINGS.fields_by_name[
        "named_consumer_strategy"
    ]._serialized_options = b"\030\001"
    _UPDATEREQ_OPTIONS.fields_by_name["stream_identifier"]._options = None
    _UPDATEREQ_OPTIONS.fields_by_name["stream_identifier"]._serialized_options = (
        b"\030\001"
    )
    _UPDATEREQ_SETTINGS.fields_by_name["revision"]._options = None
    _UPDATEREQ_SETTINGS.fields_by_name["revision"]._serialized_options = b"\030\001"
    _READREQ._serialized_start = 126
    _READREQ._serialized_end = 1047
    _READREQ_OPTIONS._serialized_start = 367
    _READREQ_OPTIONS._serialized_end = 756
    _READREQ_OPTIONS_UUIDOPTION._serialized_start = 622
    _READREQ_OPTIONS_UUIDOPTION._serialized_end = 739
    _READREQ_ACK._serialized_start = 758
    _READREQ_ACK._serialized_end = 814
    _READREQ_NACK._serialized_start = 817
    _READREQ_NACK._serialized_end = 1036
    _READREQ_NACK_ACTION._serialized_start = 974
    _READREQ_NACK_ACTION._serialized_end = 1036
    _READRESP._serialized_start = 1050
    _READRESP._serialized_end = 2094
    _READRESP_READEVENT._serialized_start = 1262
    _READRESP_READEVENT._serialized_end = 2030
    _READRESP_READEVENT_RECORDEDEVENT._serialized_start = 1616
    _READRESP_READEVENT_RECORDEDEVENT._serialized_end = 2009
    _READRESP_READEVENT_RECORDEDEVENT_METADATAENTRY._serialized_start = 1962
    _READRESP_READEVENT_RECORDEDEVENT_METADATAENTRY._serialized_end = 2009
    _READRESP_SUBSCRIPTIONCONFIRMATION._serialized_start = 2032
    _READRESP_SUBSCRIPTIONCONFIRMATION._serialized_end = 2083
    _CREATEREQ._serialized_start = 2097
    _CREATEREQ._serialized_end = 4263
    _CREATEREQ_OPTIONS._serialized_start = 2192
    _CREATEREQ_OPTIONS._serialized_end = 2560
    _CREATEREQ_STREAMOPTIONS._serialized_start = 2563
    _CREATEREQ_STREAMOPTIONS._serialized_end = 2768
    _CREATEREQ_ALLOPTIONS._serialized_start = 2771
    _CREATEREQ_ALLOPTIONS._serialized_end = 3547
    _CREATEREQ_ALLOPTIONS_FILTEROPTIONS._serialized_start = 3104
    _CREATEREQ_ALLOPTIONS_FILTEROPTIONS._serialized_end = 3516
    _CREATEREQ_ALLOPTIONS_FILTEROPTIONS_EXPRESSION._serialized_start = 3453
    _CREATEREQ_ALLOPTIONS_FILTEROPTIONS_EXPRESSION._serialized_end = 3496
    _CREATEREQ_POSITION._serialized_start = 3549
    _CREATEREQ_POSITION._serialized_end = 3610
    _CREATEREQ_SETTINGS._serialized_start = 3613
    _CREATEREQ_SETTINGS._serialized_end = 4193
    _CREATEREQ_CONSUMERSTRATEGY._serialized_start = 4195
    _CREATEREQ_CONSUMERSTRATEGY._serialized_end = 4263
    _CREATERESP._serialized_start = 4265
    _CREATERESP._serialized_end = 4277
    _UPDATEREQ._serialized_start = 4280
    _UPDATEREQ._serialized_end = 5836
    _UPDATEREQ_OPTIONS._serialized_start = 4375
    _UPDATEREQ_OPTIONS._serialized_end = 4743
    _UPDATEREQ_STREAMOPTIONS._serialized_start = 2563
    _UPDATEREQ_STREAMOPTIONS._serialized_end = 2768
    _UPDATEREQ_ALLOPTIONS._serialized_start = 4954
    _UPDATEREQ_ALLOPTIONS._serialized_end = 5151
    _UPDATEREQ_POSITION._serialized_start = 3549
    _UPDATEREQ_POSITION._serialized_end = 3610
    _UPDATEREQ_SETTINGS._serialized_start = 5217
    _UPDATEREQ_SETTINGS._serialized_end = 5766
    _UPDATEREQ_CONSUMERSTRATEGY._serialized_start = 4195
    _UPDATEREQ_CONSUMERSTRATEGY._serialized_end = 4263
    _UPDATERESP._serialized_start = 5838
    _UPDATERESP._serialized_end = 5850
    _DELETEREQ._serialized_start = 5853
    _DELETEREQ._serialized_end = 6103
    _DELETEREQ_OPTIONS._serialized_start = 5948
    _DELETEREQ_OPTIONS._serialized_end = 6103
    _DELETERESP._serialized_start = 6105
    _DELETERESP._serialized_end = 6117
    _GETINFOREQ._serialized_start = 6120
    _GETINFOREQ._serialized_end = 6372
    _GETINFOREQ_OPTIONS._serialized_start = 6217
    _GETINFOREQ_OPTIONS._serialized_end = 6372
    _GETINFORESP._serialized_start = 6374
    _GETINFORESP._serialized_end = 6477
    _SUBSCRIPTIONINFO._serialized_start = 6480
    _SUBSCRIPTIONINFO._serialized_end = 7744
    _SUBSCRIPTIONINFO_CONNECTIONINFO._serialized_start = 7376
    _SUBSCRIPTIONINFO_CONNECTIONINFO._serialized_end = 7701
    _SUBSCRIPTIONINFO_MEASUREMENT._serialized_start = 7703
    _SUBSCRIPTIONINFO_MEASUREMENT._serialized_end = 7744
    _REPLAYPARKEDREQ._serialized_start = 7747
    _REPLAYPARKEDREQ._serialized_end = 8093
    _REPLAYPARKEDREQ_OPTIONS._serialized_start = 7854
    _REPLAYPARKEDREQ_OPTIONS._serialized_end = 8093
    _REPLAYPARKEDRESP._serialized_start = 8095
    _REPLAYPARKEDRESP._serialized_end = 8113
    _LISTREQ._serialized_start = 8116
    _LISTREQ._serialized_end = 8518
    _LISTREQ_OPTIONS._serialized_start = 8207
    _LISTREQ_OPTIONS._serialized_end = 8386
    _LISTREQ_STREAMOPTION._serialized_start = 8389
    _LISTREQ_STREAMOPTION._serialized_end = 8518
    _LISTRESP._serialized_start = 8520
    _LISTRESP._serialized_end = 8616
    _PERSISTENTSUBSCRIPTIONS._serialized_start = 8619
    _PERSISTENTSUBSCRIPTIONS._serialized_end = 9593
# @@protoc_insertion_point(module_scope)
