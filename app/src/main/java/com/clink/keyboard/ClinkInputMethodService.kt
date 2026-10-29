
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
  enter.setOnClickListener{ currentInputConnection?.commitText("\n",1) }
  bottom.addView(space); bottom.addView(enter)
  root.addView(bottom)
  window?.window?.decorView?.setBackgroundColor(0)
  return root
 }
}
