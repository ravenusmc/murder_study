//Given year code
$(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_by_year', {
        a: $('input[name="year"]').val()
      }, function(data) {
        $('#results').text(data.result);
        $('input[name=year]').focus().select();
      });
      return false;
    };

    $('a#year').bind('click', submit_form);
});

//EXAMPLE
$(function() {
  var submit_form = function(e) {
    $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
      a: $('input[name="a"]').val(),
      b: $('input[name="b"]').val()
    }, function(data) {
      $('#result').text(data.result);
      $('input[name=a]').focus().select();
    });
    return false;
  };

  $('a#calculate').bind('click', submit_form);

});
