from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=True)

from member.views import MemberViewSet  # noqa isort:skip

router.register(r"member", MemberViewSet, basename="member")