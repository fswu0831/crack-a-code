var ctx = document.getElementById('myChart').getContext('2d');
var results = {{ results|tojson }};
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['第1候補', '第2候補', '第3候補', '第4候補', '第5候補'],
        datasets: [{
            label: "確率(%)",
            data: [12, 19, 3, 5, 2],
            backgroundColor:'rgba(142,123,220,1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        scales: {
            yAxes: [
                {
                  ticks: {
                    beginAtZero: true //0から始まる
                  },
                  gridLines: {
                    display: false //表示するか否か
                  },
                  scaleLabel: {
                    display: true, //表示するか否か
                  }
                }
              ],
              xAxes: [
                //y軸
                {
                  ticks: {
                    //軸のメモリ
                    beginAtZero: true //0から始まる
                  },
                  gridLines: {
                    //y軸の網線
                    display: false //表示するか否か
                  },
                  scaleLabel: {
                    //表示されるy軸の名称について
                    display: false, //表示するか否か
                  }
                }
              ],
        }
    }
});