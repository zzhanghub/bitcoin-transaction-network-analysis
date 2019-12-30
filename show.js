$.ajax({
  url: "data/graph_100.txt",
  success: function (data, status) {

    var G = new jsnx.DiGraph();
 
    G.addNodesFrom([1,2,3,4,5,6,7,8,[9,{color: '#008A00'}]], {color: '#0064C7'});
    G.addCycle([1,2,3,4,5]);
    G.addEdgesFrom([[1,9], [9,1], [9,6], [9,7], [8,2]]);
    jsnx.draw(G, {
    element: '#show', 
    withLabels: true, 
    nodeStyle: {
        fill: function(d) { 
            return d.data.color; 
        }
    }, 
    labelStyle: {fill: 'white'},
    with_edge_labels: true,
    stickyDrag: true,
    with: 700,
    height: 400
    });

  },
  error: function (data, status) {
    var G = new jsnx.DiGraph();
 
    G.addNodesFrom([1,2,3,4,5,6,7,8,[9,{color: '#008A00'}]], {color: '#0064C7'});
    G.addCycle([1,2,3,4,5]);
    G.addEdgesFrom([[1,9], [9,1], [9,6], [9,7], [8,2]]);

    jsnx.draw(G, {
    element: '#show', 
    withLabels: true, 
    nodeStyle: {
        fill: function(d) { 
            return d.data.color; 
        }
    }, 
    labelStyle: {fill: 'white'},
    stickyDrag: true,
    with_edge_labels: true,
    with: 700,
    height: 400
    });
  }
});
