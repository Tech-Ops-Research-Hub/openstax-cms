from rest_framework import viewsets

from .models import Role, Subject, K12Subject, ErrataContent, SubjectCategory, GiveBanner, BlogContentType, \
    BlogCollection, NoWebinarMessage, WebinarCollection, AssignableAvailable, AmazonBookBlurb
from .serializers import RoleSerializer, SubjectSerializer, K12SubjectSerializer, ErrataContentSerializer, \
    SubjectCategorySerializer, \
    GiveBannerSerializer, BlogContentTypeSerializer, BlogCollectionSerializer, NoWebinarMessageSerializer, \
    WebinarCollectionSerializer, AssignableAvailableSerializer, AmazonBookBlurbSerializer

from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

SPANISH_LOCALE_ID = 2
ENGLISH_LOCALE_ID = 1


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class SubjectList(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = Subject.objects.all().order_by('name')
        name = self.request.query_params.get('name', None)
        locale = self.request.query_params.get('locale', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if locale is not None:
            queryset = queryset.filter(locale=convert_locale(locale))
        return queryset

class K12SubjectList(viewsets.ReadOnlyModelViewSet):
    serializer_class = K12SubjectSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = K12Subject.objects.all()
        name = self.request.query_params.get('name', None)
        locale = self.request.query_params.get('locale', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if locale is not None:
            queryset = queryset.filter(locale=convert_locale(locale))
        return queryset

class ErrataContentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ErrataContentSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = ErrataContent.objects.all()
        book_state = self.request.query_params.get('book_state', None)
        locale = self.request.query_params.get('locale', None)
        if book_state is not None:
            queryset = queryset.filter(book_state=book_state)
        if locale is not None:
            queryset = queryset.filter(locale=convert_locale(locale))
        return queryset


class SubjectCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubjectCategorySerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = SubjectCategory.objects.all()
        subject = self.request.query_params.get('subject', None)
        locale = self.request.query_params.get('locale', None)
        if subject is not None:
            subject_id = convert_subject_name(subject)
            queryset = queryset.filter(subject=subject_id)
        if locale is not None:
            queryset = queryset.filter(locale=convert_locale(locale))
        return queryset


class GiveBannerViewSet(viewsets.ReadOnlyModelViewSet):
    # validation prevents multiple Give Banners, so this is safe
    queryset = GiveBanner.objects.all()
    serializer_class = GiveBannerSerializer


class BlogContentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogContentType.objects.all()
    serializer_class = BlogContentTypeSerializer


class BlogCollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCollection.objects.all()
    serializer_class = BlogCollectionSerializer


class NoWebinarMessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NoWebinarMessage.objects.all()
    serializer_class = NoWebinarMessageSerializer


class WebinarCollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WebinarCollection.objects.all()
    serializer_class = WebinarCollectionSerializer


class AssignableAvailableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AssignableAvailable.objects.all()
    serializer_class = AssignableAvailableSerializer


class AmazonBookBlurbViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AmazonBookBlurb.objects.all()
    serializer_class = AmazonBookBlurbSerializer


def convert_locale(locale):
    if locale == 'es':
        return SPANISH_LOCALE_ID
    return ENGLISH_LOCALE_ID


def convert_subject_name(subject):
    subjects = Subject.objects.all()
    result = subjects.filter(name=subject)
    return result[0].id

