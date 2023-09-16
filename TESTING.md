# **Clicks Backend- API**

## Testing

- [Manual Testing](#manual-testing)
    * [Posts](#posts)
    * [Events](#events)
    * [Liked Posts](#liked-posts)
    * [Comments](#comments)
    * [Reviews](#reviews)
    * [Event Likes](#event-likes)
    * [Profiles](#profiles)
- [PEP8 Validation](#pep8-validation)
    * [Posts Validation](#posts-validation)
    * [Events Validation](#events-validation)
    * [Liked Posts Validation](#liked-posts-validation)
    * [Comments Validation](#comments-validation)
    * [Reviews Validation](#reviews-validation)
    * [Event Likes Validation](#event-likes-validation)
    * [Profiles Validation](#profiles-validation)
    * [Following Validation](#following-validation)
    * [Clicks API Validation](#clicks-api-validation)
- [Known Bugs](#known-bugs)

## Manual Testing

Manual testing was completed for each app to ensure everything was working fine and all the requirements were met.

### Posts

| Status | **Posts**
|:-------:|:--------|
| &check; | Post List displays all the post created by all the user
| &check; | Posts can be edited by the user
| &check; | Post can be deleted by the user 
| &check; | Users can create a post
| &check; | Posts List can be ordered by likes_count in ascending order
| &check; | Profile List can be ordered by likes_count in descending order
| &check; | Profile List can be ordered by comments_count in ascending order
| &check; | Profile List can be ordered by  in descending order
| &check; | Posts List can filter to search for posts by entering letters or keywords

### Events

| Status | **Events**
|:-------:|:--------|
| &check; | Events List displays all the post created by all the user
| &check; | Events can be edited by the user
| &check; | Events can be deleted by the user 
| &check; | Users can create an event
| &check; | Events List can be ordered by eventlikes_count in ascending order
| &check; | Events List can be ordered by eventlikes_count in descending order
| &check; | Events List can be filtered by differnett categories
| &check; | Events List can filter to search for posts by entering letters or keywords

### Liked Posts

| Status | **Liked Posts**
|:-------:|:--------|
| &check; | Users can like a post
| &check; | Users can delete a like
| &check; | Likes Post list displays all the liked posts and total like_id.

### Comments

| Status | **Comments**
|:-------:|:--------|
| &check; | Comments List displays all the comments on posts
| &check; | Users can delete a comment
| &check; | Users can create a comment.
| &check; | Users can edit a comment.

### Reviews

| Status | **Reviews**
|:-------:|:--------|
| &check; | Review List displays all the reviews on different events
| &check; | Users can create a review.
| &check; | Users can edit a review.
| &check; | Users can delete a review.

### Event Likes

| Status | **Event Likes**
|:-------:|:--------|
| &check; | Event Like List displays all the likes on different events.
| &check; | Users can create a like on a event.
| &check; | Users can delete their like from an event.

### Profiles

| Status | **Profiles**
|:-------:|:--------|
| &check; | Profiles can be edited and deleted
| &check; | New profile can be created by the user
| &check; | List of profile is displayed to user 
| &check; | Profile List can be ordered by events_count in ascending order
| &check; | Profile List can be ordered by events_count in descending order
| &check; | Profile List can be ordered by posts_count in ascending order
| &check; | Profile List can be ordered by posts_count in descending order
| &check; | Profile List can be ordered by followed_count in ascending order
| &check; | Profile List can be ordered by followed_count in descending order
| &check; | Profile List can be ordered by following_count in ascending order
| &check; | Profile List can be ordered by following_count in descending order
| &check; | Profile List can be ordered by owner__following__created_at in ascending order
| &check; | Profile List can be ordered by owner__following__created_at in descending order
| &check; | Profile List can be ordered by owner__followed__created_at in ascending order
| &check; | Profile List can be ordered by owner__followed__created_at in descending order
| &check; | Profile List can filter to search for user by entering letters or keywords


## PEP8 Validation

I used the code institute [CI PEP8 Linter](https://pep8ci.herokuapp.com/#) to test for any errors or bugs in the code. Any error or bugs that were returned have been fixed.

### Posts Validation

**models.py file**

![post models.py](/documentation/testing/post-model.png)

**serializer.py file**

![post serializer](/documentation/testing/post-serializer.png)

**urls.py**

![post urls](/documentation/testing/post-urls.png)

**views.py**

![post views](/documentation/testing/post-view.png)

### Events Validation

**models.py file**

![Events models](/documentation/testing/events-model.png)

**serializers.py**

![Event Serializer](/documentation/testing/event-serializer.png)

**urls.py**

![Event urls](/documentation/testing/event-urls.png)

**views.py**

![Event Views](/documentation/testing/event-views.png)

### Liked Posts Validation

**models.py**

![Like posts model](/documentation/testing/likepost-model.png)

**serializers.py**

![Like posts model](/documentation/testing/likepost-serializer.png)

**urls.py**

![Like posts model](/documentation/testing/likepost-urls.png)

**views.py**

![Like posts model](/documentation/testing/likepost-views.png)

### Comments Validation

**models.py**

![Comment model](/documentation/testing/comment-model.png)

**serializers.py**

![Comment serializer](/documentation/testing/comment-serializer.png)

**urls.py**

![Comment urls](/documentation/testing/comment-urls.png)

**views.py**

![Comment views](/documentation/testing/comment-views.png)

### Reviews Validation

**models.py**

![Review models](/documentation/testing/reviews-model.png)

**serializers.py**

![Review serializer](/documentation/testing/reviews-serializer.png)

**urls.py**

![Review urls](/documentation/testing/reviews-urls.png)

**views.py**

![Review views](/documentation/testing/review-views.png)

### Event Likes Validation

**models.py**

![Event Likes models](/documentation/testing/eventlikes-model.png)

**serializers.py**

![Event Likes serializer](/documentation/testing/eventlikes-serializer.png)

**urls.py**

![Event Likes serializer](/documentation/testing/eventlikes-urls.png)

**views.py**

![Event Likes views](/documentation/testing/eventlikes-views.png)

### Profiles Validation

**models.py**

![Profiles model](/documentation/testing/profile-model.png)

**serializers.py**

![Profiles serializer](/documentation/testing/profile-serializer.png)

**urls.py**

![Profiles urls](/documentation/testing/profile-url.png)

**views.py**

![Profile views](/documentation/testing/profile-views.png)

### Following Validation

**models.py**

![Following model](/documentation/testing/following-model.png)

**serializers.py**

![Following serializer](/documentation/testing/profile-serializer.png)

**urls.py**

![Following urls](/documentation/testing/following-urls.png)

**views.py**

![Following views](/documentation/testing/profile-views.png)

### Clicks API Validation

**permissions.py**

![API model](/documentation/testing/api-permissions.png)

**serializers.py**

![API serializer](/documentation/testing/api-serializer.png)

**urls.py**

![API urls](/documentation/testing/api-urls.png)

**views.py**

![API views](/documentation/testing/api-views.png)
