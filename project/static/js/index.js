//Given year code
$(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_by_year', {
        year: $('input[name="year_value"]').val()
      }, function(data) {
        $('#results').text('There were ' + data.result + '' + ' murders in the year you entered.');
        $('input[name=year_value]').focus().select();
      });
      return false;
    };

    $('a#year').bind('click', submit_form);
});

//Code to calculate murders in a given state
$(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_by_state', {
        state: $('input[name="state_name"]').val()
      }, function(data) {
        $('#state_results').text('There were ' + data.result + '' + ' murders in the state you entered.');
        $('input[name=state_name]').focus().select();
      });
      return false;
    };

    $('a#state').bind('click', submit_form);
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
