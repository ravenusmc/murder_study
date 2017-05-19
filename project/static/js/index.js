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

//Code to calculate murders in a given state and year
$(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_by_state_year', {
        state_name: $('input[name="state_name_two"]').val(),
        year_two: $('input[name="year_two"]').val()
      }, function(data) {
        $('#state_year_results').text('There were ' + data.result + '' + ' murders in the state and year you entered.');
        $('input[name=state_name_two]').focus().select();
      });
      return false;
    };

    $('a#state_year').bind('click', submit_form);
});

//Code to look at murders by sex.
$(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_by_sex', {
        sex_one: $('input[name="sex_one"]').val(),
        sex_two: $('input[name="sex_two"]').val()
      }, function(data) {
        $('#sex_results').text(data.result[2] + '' + ' murders were committed by ' + data.result[0] + 's' + ' ' + 'on ' + data.result[1] + 's');
      });
      return false;
    };

    $('a#sex').bind('click', submit_form);

});

//This Jquery code will attach the navbar to the screen when the browser
//pases a certain limit
$(document).ready(function() {
  $(window).scroll(function () {
    //   console.log($(window).scrollTop())
    if ($(window).scrollTop() >= 115) {
      $('.graph_nav').addClass('navbar-fixed');
    }
    if ($(window).scrollTop() < 115 ) {
      $('.graph_nav').removeClass('navbar-fixed');
      console.log('Fixed Applied');
    }
  });
});
