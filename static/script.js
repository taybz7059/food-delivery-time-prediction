// 🚴 DeliverIQ - Prediction System


const form =
    document.getElementById("predictionForm");


const resultNumber =
    document.querySelector(".result-number");


const resultMessage =
    document.getElementById("resultMessage");


const predictButton =
    document.getElementById("predictButton");



form.addEventListener(
    "submit",
    async function (event) {

        // 🛑 Stop page refresh
        event.preventDefault();


        // ⏳ Loading
        predictButton.innerHTML =
            "⏳ Predicting...";

        predictButton.disabled = true;


        // 📅 Current date & time
        const now = new Date();


        // 📅 Day
        const orderDay =
            now.getDate();


        // 📅 Month
        const orderMonth =
            now.getMonth() + 1;


        // 📅 JavaScript:
        // Sunday = 0
        // Pandas:
        // Monday = 0
        const orderDayOfWeek =
            (now.getDay() + 6) % 7;


        // 📅 Weekend
        const isWeekend =
            now.getDay() === 0 ||
            now.getDay() === 6
                ? 1
                : 0;


        // ⏰ Hour
        const orderHour =
            now.getHours();


        // ⏰ Minute
        const orderMinute =
            now.getMinutes();


        // 📦 Prepare input
        const data = {

            Delivery_person_Age:
                Number(
                    document.getElementById(
                        "age"
                    ).value
                ),


            Delivery_person_Ratings:
                Number(
                    document.getElementById(
                        "rating"
                    ).value
                ),


            Road_traffic_density:
                document.getElementById(
                    "traffic"
                ).value,


            Vehicle_condition:
                Number(
                    document.getElementById(
                        "vehicleCondition"
                    ).value
                ),


            multiple_deliveries:
                Number(
                    document.getElementById(
                        "multipleDeliveries"
                    ).value
                ),


            // 📅 Automatically calculated
            order_day:
                orderDay,


            order_month:
                orderMonth,


            order_dayofweek:
                orderDayOfWeek,


            is_weekend:
                isWeekend,


            // ⏰ Automatically calculated
            order_hour:
                orderHour,


            order_minute:
                orderMinute,


            pickup_delay_min:
                Number(
                    document.getElementById(
                        "pickupDelay"
                    ).value
                ),


            distance_km:
                Number(
                    document.getElementById(
                        "distance"
                    ).value
                ),


            Weatherconditions:
                document.getElementById(
                    "weather"
                ).value,


            Type_of_order:
                document.getElementById(
                    "orderType"
                ).value,


            Type_of_vehicle:
                document.getElementById(
                    "vehicleType"
                ).value,


            Festival:
                document.getElementById(
                    "festival"
                ).value,


            City:
                document.getElementById(
                    "city"
                ).value

        };


        try {


            // 🚀 Send data to FastAPI
            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },

                        body:
                            JSON.stringify(data)

                    }
                );


            // ❌ Check response
            if (!response.ok) {

                const error =
                    await response.json();

                console.error(error);

                throw new Error(
                    "Prediction failed"
                );

            }


            // 📥 Get result
            const result =
                await response.json();


            // 🎯 Display result
            resultNumber.textContent =
                result.predicted_delivery_time;


            resultMessage.textContent =
                "Estimated delivery time based on the trained Random Forest Machine Learning model.";


            // ✨ Animation
            resultNumber.style.transform =
                "scale(1.15)";


            setTimeout(
                function () {

                    resultNumber.style.transform =
                        "scale(1)";

                },
                250
            );


        }


        catch (error) {

            console.error(error);


            resultNumber.textContent =
                "--";


            resultMessage.textContent =
                "Something went wrong. Please check your inputs and try again.";

        }


        finally {

            // 🔄 Reset button
            predictButton.innerHTML =
                "🔮 Predict Delivery Time";


            predictButton.disabled =
                false;

        }

    }
);