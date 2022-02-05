let filter = "";

$('#select-filter').change(function(){
    filter = $(this).val();

    switch(filter){
        case "price_gt":
        case "price_lt":
            $("#fs-value").show();
            break
        case "price_mod_gt":
        case "price_mod_lt":
            $("fieldset").show();
            break
        case "":
            $("fieldset").hide();
            break
    }
});

$('#btn-filter').click(function(){
    let url = new URL(window.location.protocol + "//" + window.location.host + "/stored_stock_data");

    if(filter != ""){
        url.searchParams.append("query", filter);

        if(filter == "price_gt" || filter == "price_lt"){
            url.searchParams.append("value", $("#input-value").val());
        }else{
            url.searchParams.append("value", `${$("#select-stock").val()},${$('#input-value').val()}`)
        }
    }

    console.log(url);

    window.location.href = url;
});