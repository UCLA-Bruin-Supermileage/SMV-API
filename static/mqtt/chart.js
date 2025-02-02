var Interval;
const maxValues = 10; 
var startTime;

/**************************************
TIMER FUNCTION: runs timer at top of page
***************************************/
function timer_s(seconds, minutes, hours)
{
  console.log(seconds)
  console.log(minutes)
  console.log(hours)

  var p2 = minutes; 
  var p1 = seconds; 
  var p3 = hours;
  var appendTens = document.getElementById("tens")
  var appendSeconds = document.getElementById("seconds")
  var appendHours = document.getElementById("hours")

  appendTens.innerHTML = p1;
  appendSeconds.innerHTML = p2;
  appendHours.innerHTML = p3;
  function startTimer () {
      p1++; 
      if(p1 <= 9){
        appendTens.innerHTML = "0" + p1;
      }
      
      if (p1 > 9){
        appendTens.innerHTML = p1;
      } 
      
      if (p1 > 59) {
        p2++;
        appendSeconds.innerHTML = "0" + p2;
        p1 = 0;
        appendTens.innerHTML = "0" + 0;
      }
              
      if (p2 > 59) {
          p3++;
          appendSeconds.innerHTML = "0" + 0;
          appendTens.innerHTML = "0" + 0;
          p1 = 0;
          p2 = 0;
          appendHours.innerHTML = "0" + p3;
        }
      if (p3 > 9) {
          appendHours.innerHTML = p3;
      }
      if (p2 > 9){
        appendSeconds.innerHTML = p2;
      }
    
    }
  Interval = setInterval(startTimer, 1000);
}





//defining chart daq.speed, init empty
let daqSpeed = new Chart(document.getElementById('daq.speed'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Speed of Car',
      data: [],
      borderWidth: 1,
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Car Speed (mph)',
        color: "black"
      }
   },
    scales: {
      y: {
        title: {
          display: true,
          text: "Speed (mph)",
          color: "black"
        },
        beginAtZero: true,
        grid: {
          color: "#cedade"
        }
      },
      x: {
          title: {
            display: true,
            ticks: {
              beginAtZero:true,
              min: 0,
              max: 100  
            },
            text: "Time (HH:MM:SS)",
            color: "black"
          },
        }
    }
  }
});

  //defining chart rpm, init empty
let rpm = new Chart(document.getElementById('rpm'), {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Bear 1 RPM',
        data: [],
        borderWidth: 1,
        borderColor: "#FF0000",
      }]
    },
    options: {
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          color: "black",
          display: true,
          text: 'RPM of Motor 1'
        }
     },
      scales: {
        y: {
          title: {
            color: "black",
            display: true,
            text: "RPM",
          },
          grid: {
            color: "#cedade"
          }
        },
        x: {
          title: {
            color: "black",
            display: true,
            text: "Time (HH:MM:SS)",
          },
        }
    }
  }
});
let rpm_again = new Chart(document.getElementById('rpm_again'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Bear 2 RPM',
      data:[],
      borderWidth:1,
      borderColor: "#0000FF",
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        color: "black",
        display: true,
        text: 'RPM of Motor 2'
      }
   },
    scales: {
      y: {
        title: {
          color: "black",
          display: true,
          text: "RPM",
        },
        grid: {
          color: "#cedade"
        }
      },
      x: {
        title: {
          color: "black",
          display: true,
          text: "Time (HH:MM:SS)",
        },
      }
  }
}
});

//defining chart daq.speed, init empty
let power = new Chart(document.getElementById('power_control.power'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Power',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        color: "black",
        display: true,
        text: 'Fuel Cell Power (W)'
      }
   },
    scales: {
      y: {
        title: {
          color: "black",
          display: true,
          text: "Fuel Cell Power (W)",
        },
        beginAtZero: true,
        grid: {
          color: "#cedade"
        }
      },
      x: {
          title: {
            color: "black",
            display: true,
            text: "Time (HH:MM:SS)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let current = new Chart(document.getElementById('power_control.current'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Current',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        color: "black",
        display: true,
        text: 'Fuel Cell Current (A)'
      }
   },
    scales: {
      y: {
        title: {
          color: "black",
          display: true,
          text: "Current (A)",
        },
        beginAtZero: true,
        grid: {
          color: "#cedade"
        }
      },
      x: {
          title: {
            color: "black",
            display: true,
            text: "Time (HH:MM:SS)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let voltage = new Chart(document.getElementById('power_control.voltage'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Voltage (V)',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        color: "black",
        display: true,
        text: 'Fuel Cell Voltage (V)'
      }
   },
    scales: {
      y: {
        title: {
          color: "black",
          display: true,
          text: "Voltage (V)",
        },
        beginAtZero: true,
        grid: {
          color: "#cedade"
        }
      },
      x: {
          title: {
            color: "black",
            display: true,
            text: "Time (HH:MM:SS)",
          },
        }
    }
  }
});

//defining chart daq.speed, init empty
let temp = new Chart(document.getElementById('hsmessage.temperature'), {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Fuel Cell Temperature (C)',
      data: [],
      borderWidth: 1
    }]
  },
  options: {
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        color: "black",
        display: true,
        text: 'Fuel Cell Temperature (C)'
      }
   },
    scales: {
      y: {
        title: {
          color: "black",
          display: true,
          text: "Temperature (C)",
        },
        beginAtZero: true,
        grid: {
          color: "#cedade"
        }
      },
      x: {
          title: {
            color: "black",
            display: true,
            text: "Time (HH:MM:SS)",
          },
        }
    }
  }
});
//add data to chart with label(x) and newData(y)
function addData(chart, newData, index=-1) {
  timeDiffdate = (new Date() - startTime)/1000; //ms to s
  console.log(timeDiffdate)
  var tdHr = Math.floor(timeDiffdate/3600);
  var tdMin = Math.floor((timeDiffdate-tdHr*3600)/60);
  var tdSec = Math.floor(timeDiffdate-tdHr*3600-tdMin*60);
  var label = tdHr + ":" + tdMin +":"+ tdSec;

    if (index==-1) {
      chart.data.labels.push(label);
      chart.data.datasets[0].data.push(newData)
      // chart.data.datasets.forEach((dataset) => {
      //     dataset.data.push(newData);
      // });
    }
    else {
      chart.data.labels.push(label);
      chart.data.datasets[index].data.push(newData)
    }
    if (chart.data.labels.length > maxValues)
    {
      chart.data.labels.shift();
      chart.data.datasets[0].data.shift(); //shift all datasets
      // if(chart == rpm){
      //   chart.data.datasets[1].data.shift(); //shift all datasets
      // }
    }
    chart.update('none');
}

Chart.defaults.borderColor = "#8c8b8b";
//NEW: WebSocket
let chatSocket = 0;
if (window.location.protocol == "https:") {
  chatSocket = new WebSocket(
      'wss://'
      + window.location.host
      + '/ws/teamview'
  );
} else {
  chatSocket = new WebSocket(
      'ws://'
      + window.location.host
      + '/ws/teamview'
  );
}
let ct = 0;
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    date = new Date()
    switch (data['module']) {
        case 'timing':
          //case: initial time from most recent trip
          timer_s(data['second'], data['minute'], data['hour'])
          d = new Date();
          startTime = Date.parse(`${data['date']}`)
          console.log(startTime)
          break;
        case 'daq.speed':
            //Speed Data
            addData(daqSpeed, data['content'])
            break;
        case 'bear1.rpm':
            //Motor 1 RPM data
            addData(rpm, data['content'])
            break;
        case 'bear2.rpm':
            //Motor 1 RPM data
            addData(rpm_again, data['content'])
            break;
        case 'hsmessage.temperature':
          //Motor 1 RPM data
          addData(temp, data['content'],0)
          break;
        case 'power_control.voltage':
          //Motor 1 RPM data
          addData(voltage, data['content'],0)
          break;
        case 'power_control.current':
          //Motor 1 RPM data
          addData(current, data['content'],0)
          break;
        case 'power_control.power':
          //Motor 1 RPM data
          addData(power, data['content'],0)
          break;
        //implement rest of the cases for all dashboard modules
        default:
            break;
  }
  ct++;
  console.log(ct);
};


chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};