import pathlib
base=pathlib.Path.home() / "liquid-glass-clink"
(base / "app/src/main/java/com/clink/keyboard/ui").mkdir(parents=True, exist_ok=True)

key = '''
package com.clink.keyboard.ui
import android.content.Context
import android.graphics.*
import android.os.Build
import android.util.AttributeSet
import androidx.appcompat.widget.AppCompatTextView
class LiquidGlassKey @JvmOverloads constructor(c: Context, a: AttributeSet?=null) : AppCompatTextView(c,a){
 private val paint=Paint(1)
 private val rect=RectF()
 init{
  setTextColor(Color.WHITE); textSize=19f; gravity=android.view.Gravity.CENTER
  if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.S){
   setRenderEffect(RenderEffect.createBlurEffect(28f,28f,Shader.TileMode.CLAMP))
  }
  setLayerType(LAYER_TYPE_HARDWARE,null)
 }
 override fun onSizeChanged(w:Int,h:Int,ow:Int,oh:Int){super.onSizeChanged(w,h,ow,oh); rect.set(2f,2f,w-2f,h-2f)}
 override fun onDraw(canvas: Canvas){
  val alpha=if(isPressed) 95 else 55
  paint.color=Color.argb(alpha,255,255,255)
  canvas.drawRoundRect(rect,38f,38f,paint)
  paint.style=Paint.Style.STROKE; paint.strokeWidth=2f; paint.color=Color.argb(85,255,255,255)
  canvas.drawRoundRect(rect,38f,38f,paint)
  super.onDraw(canvas)
 }
}
'''

service = '''
package com.clink.keyboard
import android.inputmethodservice.InputMethodService
import android.view.View
import android.widget.LinearLayout
import com.clink.keyboard.ui.LiquidGlassKey
class ClinkInputMethodService: InputMethodService(){
 override fun onCreateInputView(): View{
  val root=LinearLayout(this).apply{ orientation=LinearLayout.VERTICAL; setBackgroundColor(0); setPadding(8,8,8,8) }
  fun addRow(s:String){
   val row=LinearLayout(this).apply{ orientation=LinearLayout.HORIZONTAL }
   for(ch in s){
    val k=LiquidGlassKey(this).apply{ text=ch.toString(); layoutParams=LinearLayout.LayoutParams(0,135,1f).apply{setMargins(6,6,6,6)} }
    k.setOnClickListener{ currentInputConnection?.commitText(ch.toString(),1) }
    row.addView(k)
   }
   root.addView(row)
  }
  addRow("qwertyuiop"); addRow("asdfghjkl"); addRow("zxcvbnm")
  val bottom=LinearLayout(this).apply{ orientation=LinearLayout.HORIZONTAL }
  val space=LiquidGlassKey(this).apply{ text="SPACE"; layoutParams=LinearLayout.LayoutParams(0,135,3f).apply{setMargins(6,6,6,6)} }
  space.setOnClickListener{ currentInputConnection?.commitText(" ",1) }
  val enter=LiquidGlassKey(this).apply{ text="ENTER"; tag="enter"; layoutParams=LinearLayout.LayoutParams(0,135,1f).apply{setMargins(6,6,6,6)} }
  enter.setOnClickListener{ currentInputConnection?.commitText("\\n",1) }
  bottom.addView(space); bottom.addView(enter)
  root.addView(bottom)
  window?.window?.decorView?.setBackgroundColor(0)
  return root
 }
}
'''

main = '''
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
'''

(base / "app/src/main/java/com/clink/keyboard/ui/LiquidGlassKey.kt").write_text(key)
(base / "app/src/main/java/com/clink/keyboard/ClinkInputMethodService.kt").write_text(service)
(base / "app/src/main/java/com/clink/keyboard/MainActivity.kt").write_text(main)
print("All files written - real liquid glass!")

