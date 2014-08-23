$(document).ready(function(){
	$.ajax({
		url: "/get_graph_data",
		success:function(result){
			graph_data = $.parseJSON(result);
			s = new sigma({
				graph: graph_data,
				container: 'graph-container'
			});
		}
	});
});
