$(function() {
	//Botao "selecionar arquivos". Envia um click para o campo oculto
	//	File, que entao abrira a janela para escolher arquivos.
	//  Apenas uma questao estetica pois a UI do campo File ainda e' muito 'feia'
	$('#btn-chose-file').click(function() {
		$('input[id=file]').click();
	});
	
	//Quando o campo oculto File tem seu valor alterado, ele atualiza o display
	//  do campo text utilizado para mostrar o arquivo escolhido. 
	$('input[id=file]').change(function() {
	  if($(this).val() != '') {
	  	$('#fake-file-input').val($(this).val());
		$('#btn-convert').attr('disabled', false);
	  } else {
	  	$('#btn-convert').attr('disabled', 'disabled');
	  }
	});
	
	//Botao Convert. Responsavel por disparar o formulario

	$('#btn-convert').click(function() {
		$('#form-video').submit();
	});
	
	//Opcoes do plugin jQuery.Form, para callback e configuracao do post em ajax.
	//O formulario nao sera enviado por post convencional mas sim por Ajax.
	//Como nao e' possivel serializar um form multipart com javascript, utilizo um plugin para isso
	var options = { 
	    success:    function(b) { 
	        $('div.progress-bar').fadeOut();
	    },
		error:      function() {
			$('div.progress-bar').fadeOut();
		},
		beforeSubmit: function() {
			$('div.progress-bar').fadeIn();
			$('#btn-convert').attr('disabled', 'disabled');
		}
	}; 
 
	$('#form-video').ajaxForm(options);
});