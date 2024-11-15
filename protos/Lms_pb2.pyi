from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("error", "token", "courses", "code")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    COURSES_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    token: str
    courses: str
    code: str
    def __init__(self, error: _Optional[str] = ..., token: _Optional[str] = ..., courses: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class UploadCourseMaterialRequest(_message.Message):
    __slots__ = ("course", "name", "term", "filename", "data", "created")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    course: str
    name: str
    term: str
    filename: str
    data: bytes
    created: str
    def __init__(self, course: _Optional[str] = ..., name: _Optional[str] = ..., term: _Optional[str] = ..., filename: _Optional[str] = ..., data: _Optional[bytes] = ..., created: _Optional[str] = ...) -> None: ...

class GetCourseContentsRequest(_message.Message):
    __slots__ = ("course", "term")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    course: str
    term: str
    def __init__(self, course: _Optional[str] = ..., term: _Optional[str] = ...) -> None: ...

class GetCourseContentsResponse(_message.Message):
    __slots__ = ("course", "term", "data", "error")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    course: str
    term: str
    data: str
    error: str
    def __init__(self, course: _Optional[str] = ..., term: _Optional[str] = ..., data: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class UploadCourseMaterialResponse(_message.Message):
    __slots__ = ("error", "size", "code")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    size: str
    code: str
    def __init__(self, error: _Optional[str] = ..., size: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class GetCourseMaterialRequest(_message.Message):
    __slots__ = ("course", "name", "term")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    course: str
    name: str
    term: str
    def __init__(self, course: _Optional[str] = ..., name: _Optional[str] = ..., term: _Optional[str] = ...) -> None: ...

class GetCourseMaterialResponse(_message.Message):
    __slots__ = ("name", "filename", "data", "error")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename: str
    data: bytes
    error: str
    def __init__(self, name: _Optional[str] = ..., filename: _Optional[str] = ..., data: _Optional[bytes] = ..., error: _Optional[str] = ...) -> None: ...

class SubmitAssignmentRequest(_message.Message):
    __slots__ = ("studentid", "course", "assignment_name", "data", "filename")
    STUDENTID_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    studentid: str
    course: str
    assignment_name: str
    data: bytes
    filename: str
    def __init__(self, studentid: _Optional[str] = ..., course: _Optional[str] = ..., assignment_name: _Optional[str] = ..., data: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class SubmitAssignmentResponse(_message.Message):
    __slots__ = ("code", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: str
    error: str
    def __init__(self, code: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class GetSubmittedAssignmentsRequest(_message.Message):
    __slots__ = ("course", "assignment_name")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    course: str
    assignment_name: str
    def __init__(self, course: _Optional[str] = ..., assignment_name: _Optional[str] = ...) -> None: ...

class GetSubmittedAssignmentsResponse(_message.Message):
    __slots__ = ("data", "error", "code")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    error: str
    code: str
    def __init__(self, data: _Optional[bytes] = ..., error: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class CreateQueryRequest(_message.Message):
    __slots__ = ("query", "course", "reply_to")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    query: str
    course: str
    reply_to: str
    def __init__(self, query: _Optional[str] = ..., course: _Optional[str] = ..., reply_to: _Optional[str] = ...) -> None: ...

class CreateQueryResponse(_message.Message):
    __slots__ = ("error", "code")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    code: str
    def __init__(self, error: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class GetQueriesRequest(_message.Message):
    __slots__ = ("course", "term")
    COURSE_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    course: str
    term: str
    def __init__(self, course: _Optional[str] = ..., term: _Optional[str] = ...) -> None: ...

class GetQueriesResponse(_message.Message):
    __slots__ = ("code", "error", "queries")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    code: str
    error: str
    queries: str
    def __init__(self, code: _Optional[str] = ..., error: _Optional[str] = ..., queries: _Optional[str] = ...) -> None: ...

class AnswerQueryRequest(_message.Message):
    __slots__ = ("qid", "answer")
    QID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    qid: str
    answer: str
    def __init__(self, qid: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class AnswerQueryResponse(_message.Message):
    __slots__ = ("error", "code")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    code: str
    def __init__(self, error: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class AskLlmRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class AskLlmResponse(_message.Message):
    __slots__ = ("error", "reply", "code")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    error: str
    reply: str
    code: str
    def __init__(self, error: _Optional[str] = ..., reply: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class RequestVoteRequest(_message.Message):
    __slots__ = ("term", "node_id", "last_log_idx", "last_log_term")
    TERM_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_LOG_IDX_FIELD_NUMBER: _ClassVar[int]
    LAST_LOG_TERM_FIELD_NUMBER: _ClassVar[int]
    term: int
    node_id: str
    last_log_idx: int
    last_log_term: int
    def __init__(self, term: _Optional[int] = ..., node_id: _Optional[str] = ..., last_log_idx: _Optional[int] = ..., last_log_term: _Optional[int] = ...) -> None: ...

class RequestVoteResponse(_message.Message):
    __slots__ = ("term", "vote_granted")
    TERM_FIELD_NUMBER: _ClassVar[int]
    VOTE_GRANTED_FIELD_NUMBER: _ClassVar[int]
    term: int
    vote_granted: bool
    def __init__(self, term: _Optional[int] = ..., vote_granted: bool = ...) -> None: ...

class AppendEntriesRequest(_message.Message):
    __slots__ = ("term", "leader_id", "prev_log_idx", "prev_log_term", "entries", "leader_commit_idx")
    TERM_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    PREV_LOG_IDX_FIELD_NUMBER: _ClassVar[int]
    PREV_LOG_TERM_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    LEADER_COMMIT_IDX_FIELD_NUMBER: _ClassVar[int]
    term: int
    leader_id: str
    prev_log_idx: int
    prev_log_term: int
    entries: str
    leader_commit_idx: int
    def __init__(self, term: _Optional[int] = ..., leader_id: _Optional[str] = ..., prev_log_idx: _Optional[int] = ..., prev_log_term: _Optional[int] = ..., entries: _Optional[str] = ..., leader_commit_idx: _Optional[int] = ...) -> None: ...

class AppendEntriesResponse(_message.Message):
    __slots__ = ("term", "success")
    TERM_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    term: int
    success: bool
    def __init__(self, term: _Optional[int] = ..., success: bool = ...) -> None: ...

class GetLeaderRequest(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: int
    def __init__(self, ack: _Optional[int] = ...) -> None: ...

class GetLeaderResponse(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    def __init__(self, node_id: _Optional[str] = ...) -> None: ...
