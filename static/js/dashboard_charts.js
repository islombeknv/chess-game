am5.ready(function () {
    let root = am5.Root.new("applicants_chart");

    const myTheme = am5.Theme.new(root);

    myTheme.rule("AxisLabel", ["minor"]).setAll({
        dy: 1
    });

    myTheme.rule("Grid", ["minor"]).setAll({
        strokeOpacity: 0.08
    });

    root.setThemes([
        am5themes_Animated.new(root),
        myTheme
    ]);

    let chart = root.container.children.push(am5xy.XYChart.new(root, {
        panX: false,
        panY: false,
        wheelX: "panX",
        wheelY: "zoomX",
        paddingLeft: 0
    }));


    let cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
        behavior: "zoomX"
    }));
    cursor.lineY.set("visible", false);

    let xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
        maxDeviation: 0,
        baseInterval: {
            timeUnit: "day",
            count: 1
        },
        renderer: am5xy.AxisRendererX.new(root, {
            minorGridEnabled: true,
            minGridDistance: 200,
            minorLabelsEnabled: true
        }),
        tooltip: am5.Tooltip.new(root, {})
    }));

    xAxis.set("minorDateFormats", {
        day: "dd",
        month: "MM"
    });

    let yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
        renderer: am5xy.AxisRendererY.new(root, {})
    }));


    let series = chart.series.push(am5xy.LineSeries.new(root, {
        name: "Series",
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        tooltip: am5.Tooltip.new(root, {
            labelText: "{valueY}"
        })
    }));

    series.bullets.push(function () {
        var bulletCircle = am5.Circle.new(root, {
            radius: 5,
            fill: series.get("fill")
        });
        return am5.Bullet.new(root, {
            sprite: bulletCircle
        })
    })

    chart.set("scrollbarX", am5.Scrollbar.new(root, {
        orientation: "horizontal"
    }));


    series.data.setAll(applicants_chart_data);

    series.appear(1000);
    chart.appear(1000, 100);

    root._logo.dispose();

});

am5.ready(function () {
    let root = am5.Root.new("departments_chart");

    root.setThemes([
        am5themes_Animated.new(root)
    ]);

    let chart = root.container.children.push(
        am5percent.PieChart.new(root, {
            endAngle: 270
        })
    );

    let series = chart.series.push(
        am5percent.PieSeries.new(root, {
            valueField: "value",
            categoryField: "category",
            endAngle: 270
        })
    );

    series.states.create("hidden", {endAngle: -90});

    series.data.setAll(departments_chart_data);

    series.appear(1000, 100);

    root._logo.dispose();

});
