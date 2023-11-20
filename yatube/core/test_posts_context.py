def post_test_context(response, text, author, group=None, image=None):

    first_object = response.context['page_obj'][0]
    test_data = {
        first_object.text: text,
        first_object.author.username: author,
    }
    if group is not None:
        test_data[first_object.group.title] = group

    elif image is not None:
        test_data[first_object.image] = image

    return test_data
