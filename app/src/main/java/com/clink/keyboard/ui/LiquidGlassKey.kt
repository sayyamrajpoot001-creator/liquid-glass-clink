
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
