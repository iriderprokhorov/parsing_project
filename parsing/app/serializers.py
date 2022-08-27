from rest_framework import serializers

from .models import News, Tag, TagNews


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "pub_date",
            "tag_ext",
            "tags",
        )

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        news = News.objects.create(**validated_data)

        for tag in tags:
            current_tag, status = Tag.objects.get_or_create(**tag)
            TagNews.objects.create(tag=current_tag, news=news)
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.tag_ext = validated_data.get("tag_ext", instance.tag_ext)

        tags_data = validated_data.get("tags", instance.tags)
        news = News.objects.get(id=instance.id)
        TagNews.objects.filter(news=news).all().delete()
        for tag in tags_data:
            current_tag, status = Tag.objects.get_or_create(**tag)
            TagNews.objects.create(news=news, tag=current_tag)
        instance.save()
        return instance
