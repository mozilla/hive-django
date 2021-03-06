$(function() {
  $("[data-find-url]").each(function() {
    var name = $(this).attr('name');
    var url = $(this).attr('data-find-url');

    $(this).typeahead({
      hint: true,
      highlight: true,
      minLength: 2
    }, {
      name: name,
      displayKey: 'value',
      source: function findMatches(q, cb) {
        $.getJSON(url, {query: q}, cb);
      }
    }).on('typeahead:selected typeahead:autocompleted', function(e, sugg) {
      window.location = sugg.url;
    }).on('keypress', function(e) {
      // http://code.tutsplus.com/tutorials/enhancing-the-search-form-with-typeaheadjs--wp-30844
      if (e.which == 13) {
        $(this).parents("form").submit();
        return false;
      }
    }).typeahead('val', '');
  });
});
