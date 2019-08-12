"use strict";
var botui = new BotUI("dentist-chatbot");
var url = "http://localhost:8080/chatbot/message";

botui.message
  .add({
    content: "Hello I am a dentist chatbot! How can I help you"
  })
  .then(function() {
    startscreenOptions();
  });

const startscreenOptions = () => {
  botui.action
    .button({
      action: [
        {
          text: "i want to check available dentists",
          value: "getAllDentists"
        },
        {
          text: "I want to check dentist detial information",
          value: "getDentistInfo"
        },
        {
          text: "i want to check available timeslots specific dentist",
          value: "getTimeslot"
        },
        {
          text: "I want to make a booking",
          value: "addBooking"
        },
        {
          text: "I want to cancel a booking",
          value: "cancel a booking"
        },
        {
          text: "Others",
          value: "Others"
        }
      ]
    })
    .then(function(res) {
      if (res.text === "I want to check dentist detial information") {
        checkDentistDetial();
      } else if (
        res.text === "i want to check available timeslots specific dentist"
      ) {
        checkDentistTimeslot();
      } else if (res.text === "I want to make a booking") {
        createBooking();
      } else if (res.text === "i want to check available dentists") {
        getAllDentists(res.text);
      } else if (res.text === "I want to cancel a booking") {
        cancelBooking();
      } else if (res.text === "Others") {
        otherMessage();
      }
    });
};

const createBooking = () => {
  var dentistId = 1;
  var patientName = "Sam";
  var phoneNumber = "0435233333";
  var bookingDate = "2019-08-08";
  var startTime = "10:30";
  var endTime = "11:30";
  var message = undefined;
  botui.message
    .bot({
      content: "Please enter dentist Id:"
    })
    .then(() => {
      return botui.action.text({
        action: {
          delay: 500,
          placeholder: "dentist Id",
          value: dentistId
        }
      });
    })
    .then(res => {
      dentistId = res.value;
      botui.message
        .bot({
          content: "Please enter your name"
        })
        .then(() => {
          return botui.action.text({
            action: {
              delay: 500,
              placeholder: "your name",
              value: patientName
            }
          });
        })
        .then(res => {
          patientName = res.value;
          botui.message
            .bot({
              content: "Please enter your phonenumber"
            })
            .then(() => {
              return botui.action.text({
                action: {
                  placeholder: "phonenumber",
                  value: phoneNumber
                }
              });
            })
            .then(res => {
              phoneNumber = res.value;
              botui.message
                .bot({
                  content: "Please enter bookingdate (i.e 2019-08-08)"
                })
                .then(() => {
                  return botui.action.text({
                    action: {
                      placeholder: "bookingdate",
                      value: bookingDate
                    }
                  });
                })
                .then(res => {
                  bookingDate = res.value;
                  botui.message
                    .bot({
                      content: "Please enter bookingdate start time (i.e 10:30)"
                    })
                    .then(() => {
                      return botui.action.text({
                        action: {
                          placeholder: "start time",
                          value: startTime
                        }
                      });
                    })
                    .then(res => {
                      startTime = res.value;
                      botui.message
                        .bot({
                          content: "Please enter endtime (i.e 11:30)"
                        })
                        .then(() => {
                          return botui.action.text({
                            action: {
                              placeholder: "end time",
                              value: endTime
                            }
                          });
                        })
                        .then(res => {
                          endTime = res.value;
                          message =
                            "i want to make a booking with " +
                            dentistId +
                            " from " +
                            startTime +
                            " to " +
                            endTime +
                            " at " +
                            bookingDate +
                            " my name is " +
                            patientName +
                            " and the contact number is " +
                            phoneNumber;
                          var content =
                            "dentistId: " +
                            dentistId +
                            " Your Name: " +
                            patientName +
                            " Phone number: " +
                            phoneNumber +
                            " booking date" +
                            bookingDate +
                            " start time: " +
                            startTime +
                            " end time: " +
                            endTime;
                          botui.message
                            .bot({
                              delay: 500,
                              content: content
                            })
                            .then(() => {
                              return botui.action
                                .button({
                                  action: [
                                    {
                                      icon: "check",
                                      text: "Confirm",
                                      value: "confirm"
                                    },
                                    {
                                      icon: "Exit",
                                      text: "Cancel",
                                      value: "cancel"
                                    }
                                  ]
                                })
                                .then(res => {
                                  if (res.value === "confirm") {
                                    return axios
                                      .post(url, {
                                        message: message
                                      })
                                      .then(function(response) {
                                        console.log(response)
                                        var data = response.data;
                                        formatResultToMessage(data);
                                        confirmDialog();
                                      });
                                  }else{
                                    startscreenOptions()
                                  }
                                });
                            });
                        });
                    });
                });
            });
        });
    })
    .catch(error => {
      console.log(error);
    });
};

const confirmDialog = () => {
  botui.action
    .button({
      action: [
        {
          text: "Go Back",
          value: true
        }
      ]
    })
    .then(response => {
      if (response.value === true) {
        startscreenOptions();
      }
    });
};

const formatResultToMessage = content => {
  botui.message.add({
    content: content
  });
};

const checkDentistDetial = () => {
  botui.message
    .bot({
      content: "Please enter the name"
    })
    .then(() => {
      return botui.action.text({
        action: {
          placeholder: "dentist name"
        }
      });
    })
    .then(res => {
      const dentistId = res.value;
      var message =
        "i want to see the details information of the dentist " + dentistId;
      axios
        .post(url, {
          message: message
        })
        .then(response => response.data)
        .then(response => {
          if (response.includes("[")) {
            var formatStr = formatStringToObj(response);
            var objArr = [];
            console.log(formatStr);
            if (formatStr.includes("},")) {
              objArr = formatStrToArr(formatStr);
            } else {
              objArr.push(JSON.parse(formatStr));
            }
            for (let obj of objArr) {
              for (let key in obj) {
                var content = key + ":" + obj[key];
                formatResultToMessage(content);
              }
            }
          } else {
            formatResultToMessage(response);
          }
          confirmDialog();
        })
    })
    .catch(error => {
      formatResultToMessage(error);
      confirmDialog();
    });
};

const formatStringToObj = str => {
  var info = str.replace("[", "").replace("]", "");
  var obj = "";
  for (let i = 0; i < info.length; i++) {
    var temp = undefined;
    if (info[i] == "'") {
      temp = '"';
    } else {
      temp = info[i];
    }
    var obj = obj + temp;
  }
  return obj;
};

const getAllDentists = message => {
  axios
    .post(url, {
      message: message
    })
    .then(response => response.data)
    .then(data => {
      var obj = formatStringToObj(data);
      var formatArr = formatStrToArr(obj);
      for (obj of formatArr) {
        var content = "id: " + obj["dentistId"] + " name: " + obj["name"];
        formatResultToMessage(content);
      }
      confirmDialog();
    })
    .catch(error => {
      console.log(error);
    });
};

const checkDentistTimeslot = () => {
  botui.message
    .bot({
      content: "Please enter the dentist id"
  }).then(()=>{
    return botui.action
    .text({
      action: {
        placeholder: "dentist id"
      }
    })
  })  
    .then(res => {
      const dentistId = res.value;
      var message = "i want to check " + dentistId + " available timeslots";
      return message;
    })
    .then(message => {
      axios
        .post(url, {
          message: message
        })
        .then(response => response.data)
        .then(data => {
          var obj = formatStringToObj(data);
          var formatArr = formatStrToArr(obj);
          for (let time of formatArr) {
            var content =
              formatTime(time["start"]) + "-" + formatTime(time["end"]);
            formatResultToMessage(content);
          }
          confirmDialog();
        });
    })
    .catch(error => {
      console.log(error)
    });
};

const formatStrToArr = arrStr => {
  var objArr = arrStr.split("},");
  var formatArr = [];
  for (let obj of objArr) {
    var formatObj = undefined;
    if (!obj.includes("}")) {
      formatObj = JSON.parse(obj + "}");
    } else {
      formatObj = JSON.parse(obj);
    }
    formatArr.push(formatObj);
  }
  return formatArr;
};

const formatTime = time => {
  return time.replace("T", " ").replace("Z", " ");
};

const otherMessage = () => {
  botui.action
    .text({
      action: {
        placeholder: "",
        value: "Hello bot"
      }
    })
    .then(message => {
      axios
        .post(url, {
          message: message.value
        })
        .then(function(response) {
          formatResultToMessage(response.data);
          confirmDialog();
        });
    })
    .catch(error => {
      console.log(error);
    });
};

const cancelBooking = () => {
  botui.message
    .bot({
      content: "Please enter the booking id"
    })
    .then(() => {
      return botui.action.text({
        action: {
          placeholder: "booking id"
        }
      });
    })
    .then(res => {
      console.log(res)
      var request = "i want to cancel my booking " + res.value;
      return axios
        .post(url, {
          message: request
        })
        .then(function(response) {
          formatResultToMessage(response.data);
          confirmDialog();
        });
    })
    .catch(error => {
      console.log(error);
    });
};
