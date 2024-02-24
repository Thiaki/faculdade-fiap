package br.com.fiap.aula03

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import br.com.fiap.aula03.ui.theme.Aula03Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Aula03Theme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    CounterScreen()
                }
            }
        }
    }
}

@Composable
fun CounterScreen() {

    var idade = remember {
        mutableStateOf(0)
    }

    var situacaoIdade = remember(idade.value) {
        if (idade.value > 17){
            mutableStateOf("Você é MAIOR de idade")
        }
        else{
            mutableStateOf("Você é MENOR de idade")
        }
    }

    fun maxIdade() {
        if (idade.value < 130){
            idade.value += 1
        }
    }

    fun minIdade() {
        if (idade.value > 0){
            idade.value -= 1
        }
    }

    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "Qual a sua idade?",
            fontSize = 24.sp,
            color = Color(0xFFAD1F4E),
            fontWeight = FontWeight.Bold
        )
        Text(
            text = "Aperte os botões para informar a sua idade.",
            fontSize = 12.sp
        )
        Spacer(
            modifier = Modifier.height(32.dp)
        )
        Text(
            text = "${idade.value}",
            fontSize = 48.sp,
            fontWeight = FontWeight.Bold
        )
        Spacer(
            modifier = Modifier.height(32.dp)
        )
        Row() {
            Button(
                onClick = { minIdade() },
                modifier = Modifier.size(84.dp),
                shape = RoundedCornerShape(8.dp),
                colors = ButtonDefaults.buttonColors(Color(0xFFAD1F4E))
            ) {
                Text(text = "-", fontSize = 40.sp)
            }
            Spacer(
                modifier = Modifier.width(32.dp)
            )
            Button(
                onClick = { maxIdade() },
                modifier = Modifier.size(84.dp),
                shape = RoundedCornerShape(8.dp),
                colors = ButtonDefaults.buttonColors(Color(0xFFAD1F4E))
            ) {
                Text(text = "+", fontSize = 40.sp)
            }
        }
        Spacer(
            modifier = Modifier.height(32.dp)
        )
        Text(
            text= "${situacaoIdade.value}",
            fontSize = 24.sp,
            color = Color(0xFFAD1F4E),
            fontWeight = FontWeight.Bold
        )
    }
}
