package br.com.fiap.appcoletadelixo.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import br.com.fiap.appcoletadelixo.ui.theme.FontKarla

@Composable
fun SearchScreen(navController: NavController) {

    var cep = remember {
        mutableStateOf("")
    }

    var showDialog = remember{
        mutableStateOf(false)
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color(0xFF8EA68D))
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .height(70.dp)
                .background(Color(0xFF21400B))
        ) {}

        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(horizontal = 16.dp)
                .wrapContentHeight(Alignment.CenterVertically),
            verticalArrangement = Arrangement.Center
        ) {
            OutlinedTextField(
                value = cep.value,
                onValueChange = {
                    newValue ->
                    val numericValue = newValue.filter { it.isDigit() }
                    cep.value = numericValue },
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color(0xFF5F8C1C), shape = RoundedCornerShape(16.dp))
                    .border(width = 1.dp,color = Color(0xFF5F8C1C),shape = RoundedCornerShape(16.dp)),
                placeholder = {
                    Text(
                        text = "Digite seu CEP",
                        fontFamily = FontKarla,
                        color = Color.White,
                        fontSize = 18.sp,
                        fontWeight = FontWeight.W700,
                    )
                },
                shape = RoundedCornerShape(16.dp),
                textStyle = TextStyle(
                    fontFamily = FontKarla,
                    color = Color.White,
                    fontSize = 18.sp,
                    fontWeight = FontWeight.W700,
                ),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )

            Spacer(modifier = Modifier.height(48.dp))

            Button(
                onClick = {
                    val enteredCep = cep.value.toIntOrNull()
                    if (enteredCep in 0..99999999) {
                        navController.navigate("result/${enteredCep}")}
                    else{
                        showDialog.value = true
                    }
                },
                modifier = Modifier
                    .align(Alignment.CenterHorizontally)
                    .size(width = 200.dp, height = 60.dp),
                shape = RoundedCornerShape(16.dp),
                colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF5F8C1C))
            ) {
                Text(
                    text = "Enviar ${cep.value}",
                    fontSize = 26.sp,
                    fontWeight = FontWeight.W700,
                    fontFamily = FontKarla,
                    color = Color.White
                )
            }
        }
    }
    if (showDialog.value) {
        AlertDialog(
            onDismissRequest = { showDialog.value = false },
            title = {
                Text("CEP Inválido")
            },
            text = {
                Text("Por favor, insira um CEP válido.")
            },
            confirmButton = {
                Button(
                    onClick = { showDialog.value = false }
                ) {
                    Text("OK")
                }
            }
        )
    }
}