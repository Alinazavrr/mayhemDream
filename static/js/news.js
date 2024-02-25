// static/js/news.js

$(document).ready(function() {
    // Toggle visibility of create news form
    $('#showCreateFormBtn').click(function() {
      $('#createNewsForm').toggle();
    });
  
    // AJAX for creating new news
    $('#createNewsForm').submit(function(e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: '/news/',
        data: $(this).serialize(),
        success: function(response) {
          if (response.success) {
            console.log(response.message);
            location.reload();
          } else {
            console.error(response.errors);
          }
        },
        error: function(error) {
          console.error('AJAX error:', error);
        }
      });
    });
  
    // AJAX for updating news
    $('.updateBtn').click(function() {
      var newsId = $(this).data('id');
      var newsTitle = $(this).data('title');
      var newsContent = $(this).data('content');
      var newsImage = $(this).data('image');
  
      // Implement the logic for updating news using the obtained data
      // ...
  
      // Example: filling a form with the data
      $('#updateForm').find('#id_title').val(newsTitle);
      $('#updateForm').find('#id_content').val(newsContent);
      $('#updateForm').find('#id_image').val(newsImage);
      // ...
    });
  
    // AJAX for deleting news
    $('.deleteBtn').click(function() {
      var newsId = $(this).data('id');
  
      if (confirm('Точно хотите удалить новость?')) {
        $.ajax({
          type: 'POST',
          url: '/news/update_delete/',
          data: {
            'delete_news': true,
            'id': newsId,
            csrfmiddlewaretoken: '{{ csrf_token }}'
          },
          success: function(response) {
            if (response.success) {
              console.log(response.message);
              location.reload();
            } else {
              console.error(response.message);
            }
          },
          error: function(error) {
            console.error('AJAX error:', error);
          }
        });
      }
    });
  });
  