package br.com.fiap.aula05

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.sp
import br.com.fiap.aula05.ui.theme.Aula05Theme
import br.com.fiap.aula05.ui.theme.KodeMono

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Aula05Theme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    BasicComponentsScreen()
                }
            }
        }
    }
}

@Composable
fun BasicComponentsScreen() {

    var textFieldValue = remember {
        mutableStateOf("")
    }

    Column (modifier = Modifier
        .fillMaxWidth()
        .background(Color.Black)
    ) {
        Text(
            modifier = Modifier
                .fillMaxWidth(),
            text = "Fiap",
            fontSize = 32.sp,
            fontWeight = FontWeight.Bold,
            color = Color(0xFFED145B),
            fontFamily = KodeMono,
            textAlign = TextAlign.Center
        )
        Text(
            modifier = Modifier
                .align(Alignment.CenterHorizontally),
            text = "Desenvolvendo aplicações Android",
            fontSize = 16.sp,
            fontWeight = FontWeight.SemiBold,
            color = Color.White,
            fontFamily = KodeMono
        )
        TextField(
            modifier = Modifier
                .fillMaxWidth(),
            value = textFieldValue.value,
            onValueChange = {
                novoValor -> textFieldValue.value = novoValor
            }
        )
    }
}
