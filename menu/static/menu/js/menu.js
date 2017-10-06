function setup(){
	
	var vBread = $("#bread").val();
	vBread = vBread || 0;
	vBread = vBread * bread;
	
	var vFish = $("#fish").val();
	vFish = vFish || 0;
	vFish = vFish * fish;
	
	var vRice = $("#rice").val();
	vRice = vRice || 0;
	vRice = vRice * rice;
	
	var vSalad = $("#salad").val();
	vSalad = vSalad || 0;
	vSalad = vSalad * csalad;
	
	var vTsoup = $("#tsoup").val();
	vTsoup = vTsoup || 0;
	vTsoup = vTsoup * tsoup;
	
	var vTvsoup = $("#tvsoup").val();
	vTvsoup = vTvsoup || 0;
	vTvsoup = vTvsoup * tvsoup;
	
	var vVsoup = $("#vsoup").val();
	vVsoup = vVsoup || 0;
	vVsoup = vVsoup * vsoup;
	
	var vBeverage = $("#beverage").val();
	vBeverage = vBeverage || 0;
	vBeverage = vBeverage * beverage;
	
	var total = vBread + vFish + vRice + vTsoup + vTvsoup + vVsoup + vBeverage;
	
	var d = new Date(document.getElementById('id_order-delivery_date').value);
    var day = d.getDay();
	
	if (day == 6){day = 0;}
	if (day < 6){day++;}
	
	if (day == 0){
		var surcharge = total * charge;
	}else if (day == 6){
		var surcharge = total * charge;
	}else{
		var surcharge = 0;
	}
	surcharge = surcharge.toFixed(2)
	
	alert(day);
	
	return [total,surcharge]
}

$(document).ready(function() {

	$('#id_order-ordered_by').hide();
	$('#id_order-total').hide();
	$('#id_order-surcharge').hide();
	$('#reset').hide();
	$('#submit').hide();

	$('#button').click(function(){
		var total;
		var surcharge;
	
		var a = setup();
		total = a[0];
		surcharge = a[1];
		$('#id_order-ordered_by').val($('#id_order-email').val());
		$('#id_order-total').val(total);
		$('#id_order-surcharge').val(surcharge);
		$('#id_order-ordered_by').show();
		$('#id_order-total').show();
		$('#id_order-surcharge').show();
		$('#reset').show();
		$('#submit').show();
		
		$('#form :input').prop("readonly", true);
	});
	
	$('#submit').click(function(){
		$('#page').load("/vieworder");
	});
});
