## Subquery() expressions

Subquery 표현식을 사용해서 QuerySet에 명시적으로 서브쿼리를 추가할 수 있다.

예를 들어 포스트에 새로운 답글을 작성한 사용자의 이메일 주소를 갖고 있는 포스트를 조회하려면

```
from django.db.models import OuterRef, Subquery
newest = Comment.objects.filter(post=OuterRef('pk')).order_by('-created_at')
Post.objects.annotate(newest_commenter_email=Subquery(newest.values('email')[:1]))
```

쿼리 최적화를 위해 해야 할 일
[ ] prefetch_related 함수가 의도대로 쿼리 생성하는지 확인
[ ] 쿼리 cached 에서 파이썬으로 필터링 수행하기
[ ] 쿼리 호출 개선 어느정도 이루어지는지 확인

``` query
SELECT
    "wendzi_post"."id",
    "wendzi_post"."owner_id",
    "wendzi_post"."type",
    "wendzi_post"."title",
    "wendzi_post"."description",
    "wendzi_post"."pay",
    "wendzi_post"."price",
    "wendzi_post"."status",
    "wendzi_post"."sell_count", "wendzi_post"."free_shipping", "wendzi_post"."duration", "wendzi_post"."shipping_price", "wendzi_post"."verified", "wendzi_post"."address_id", "wendzi_post"."productgroup_id","wendzi_post"."discount_price", "wendzi_post"."coupon_discount", "wendzi_post"."materials", "wendzi_post"."included", "wendzi_post"."quantity_type", "wendzi_post"."quantity", "wendzi_post"."created", "wendzi_post"."updated" FROM "wendzi_post"
```