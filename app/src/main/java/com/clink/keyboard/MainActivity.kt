
package com.clink.keyboard
import android.content.Intent
import android.os.Bundle
import android.provider.Settings
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
class MainActivity: AppCompatActivity(){
 override fun onCreate(b: Bundle?){
  super.onCreate(b); setContentView(R.layout.activity_main)
  findViewById<Button>(R.id.btnEnable).setOnClickListener{ startActivity(Intent(Settings.ACTION_INPUT_METHOD_SETTINGS)) }
 }
}
