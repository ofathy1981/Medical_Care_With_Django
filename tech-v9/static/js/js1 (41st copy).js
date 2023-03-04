
$(function () {$('#container1').highcharts({
     
            chart: {type: 'column'},
            title: {text: 'Statistics Analysis Diagram of HardWare Maintainace Requests'},
            subtitle: {text: 'Source: Comapany Management Sector'},
            xAxis: {categories: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']},
            yAxis: {min: 0,title: {text: 'Rainfall (mm)'}},
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'information',
                data: [44, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]  }] }); });
