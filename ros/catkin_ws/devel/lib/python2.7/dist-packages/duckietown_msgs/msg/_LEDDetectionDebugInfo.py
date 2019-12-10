# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from duckietown_msgs/LEDDetectionDebugInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import duckietown_msgs.msg
import std_msgs.msg
import genpy
import sensor_msgs.msg

class LEDDetectionDebugInfo(genpy.Message):
  _md5sum = "be212adc91f6527a99fc828df2018200"
  _type = "duckietown_msgs/LEDDetectionDebugInfo"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 state # 0: idle, 1: capturing, 2: processing
float32 capture_progress

uint32[2] cell_size
float32[4] crop_rect_norm

sensor_msgs/CompressedImage variance_map
Vector2D[] candidates

LEDDetectionArray led_all_unfiltered

================================================================================
MSG: sensor_msgs/CompressedImage
# This message contains a compressed image

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image

string format        # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png
uint8[] data         # Compressed image buffer

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: duckietown_msgs/Vector2D
float32 x
float32 y

================================================================================
MSG: duckietown_msgs/LEDDetectionArray
LEDDetection[] detections
================================================================================
MSG: duckietown_msgs/LEDDetection
time timestamp1		# initial timestamp of the camera stream used 
time timestamp2		# final timestamp of the camera stream used 
Vector2D pixels_normalized
float32 frequency 
string color        # will be ‘r’, ‘g’ or ‘b’ 
float32 confidence  # some value of confidence for the detection (TBD)

# for debug/visualization
float64[] signal_ts
float32[] signal
float32[] fft_fs
float32[] fft
"""
  __slots__ = ['state','capture_progress','cell_size','crop_rect_norm','variance_map','candidates','led_all_unfiltered']
  _slot_types = ['uint8','float32','uint32[2]','float32[4]','sensor_msgs/CompressedImage','duckietown_msgs/Vector2D[]','duckietown_msgs/LEDDetectionArray']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       state,capture_progress,cell_size,crop_rect_norm,variance_map,candidates,led_all_unfiltered

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LEDDetectionDebugInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.state is None:
        self.state = 0
      if self.capture_progress is None:
        self.capture_progress = 0.
      if self.cell_size is None:
        self.cell_size = [0] * 2
      if self.crop_rect_norm is None:
        self.crop_rect_norm = [0.] * 4
      if self.variance_map is None:
        self.variance_map = sensor_msgs.msg.CompressedImage()
      if self.candidates is None:
        self.candidates = []
      if self.led_all_unfiltered is None:
        self.led_all_unfiltered = duckietown_msgs.msg.LEDDetectionArray()
    else:
      self.state = 0
      self.capture_progress = 0.
      self.cell_size = [0] * 2
      self.crop_rect_norm = [0.] * 4
      self.variance_map = sensor_msgs.msg.CompressedImage()
      self.candidates = []
      self.led_all_unfiltered = duckietown_msgs.msg.LEDDetectionArray()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_Bf().pack(_x.state, _x.capture_progress))
      buff.write(_get_struct_2I().pack(*self.cell_size))
      buff.write(_get_struct_4f().pack(*self.crop_rect_norm))
      _x = self
      buff.write(_get_struct_3I().pack(_x.variance_map.header.seq, _x.variance_map.header.stamp.secs, _x.variance_map.header.stamp.nsecs))
      _x = self.variance_map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.variance_map.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.variance_map.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.candidates)
      buff.write(_struct_I.pack(length))
      for val1 in self.candidates:
        _x = val1
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
      length = len(self.led_all_unfiltered.detections)
      buff.write(_struct_I.pack(length))
      for val1 in self.led_all_unfiltered.detections:
        _v1 = val1.timestamp1
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v2 = val1.timestamp2
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v3 = val1.pixels_normalized
        _x = _v3
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        buff.write(_get_struct_f().pack(val1.frequency))
        _x = val1.color
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_get_struct_f().pack(val1.confidence))
        length = len(val1.signal_ts)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.signal_ts))
        length = len(val1.signal)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.signal))
        length = len(val1.fft_fs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.fft_fs))
        length = len(val1.fft)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.fft))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.variance_map is None:
        self.variance_map = sensor_msgs.msg.CompressedImage()
      if self.candidates is None:
        self.candidates = None
      if self.led_all_unfiltered is None:
        self.led_all_unfiltered = duckietown_msgs.msg.LEDDetectionArray()
      end = 0
      _x = self
      start = end
      end += 5
      (_x.state, _x.capture_progress,) = _get_struct_Bf().unpack(str[start:end])
      start = end
      end += 8
      self.cell_size = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 16
      self.crop_rect_norm = _get_struct_4f().unpack(str[start:end])
      _x = self
      start = end
      end += 12
      (_x.variance_map.header.seq, _x.variance_map.header.stamp.secs, _x.variance_map.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.variance_map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.variance_map.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.variance_map.format = str[start:end].decode('utf-8')
      else:
        self.variance_map.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.variance_map.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.candidates = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.Vector2D()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        self.candidates.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.led_all_unfiltered.detections = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.LEDDetection()
        _v4 = val1.timestamp1
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v5 = val1.timestamp2
        _x = _v5
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v6 = val1.pixels_normalized
        _x = _v6
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        start = end
        end += 4
        (val1.frequency,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.color = str[start:end].decode('utf-8')
        else:
          val1.color = str[start:end]
        start = end
        end += 4
        (val1.confidence,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.signal_ts = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.signal = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.fft_fs = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.fft = struct.unpack(pattern, str[start:end])
        self.led_all_unfiltered.detections.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_Bf().pack(_x.state, _x.capture_progress))
      buff.write(self.cell_size.tostring())
      buff.write(self.crop_rect_norm.tostring())
      _x = self
      buff.write(_get_struct_3I().pack(_x.variance_map.header.seq, _x.variance_map.header.stamp.secs, _x.variance_map.header.stamp.nsecs))
      _x = self.variance_map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.variance_map.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.variance_map.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.candidates)
      buff.write(_struct_I.pack(length))
      for val1 in self.candidates:
        _x = val1
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
      length = len(self.led_all_unfiltered.detections)
      buff.write(_struct_I.pack(length))
      for val1 in self.led_all_unfiltered.detections:
        _v7 = val1.timestamp1
        _x = _v7
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v8 = val1.timestamp2
        _x = _v8
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v9 = val1.pixels_normalized
        _x = _v9
        buff.write(_get_struct_2f().pack(_x.x, _x.y))
        buff.write(_get_struct_f().pack(val1.frequency))
        _x = val1.color
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_get_struct_f().pack(val1.confidence))
        length = len(val1.signal_ts)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.signal_ts.tostring())
        length = len(val1.signal)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.signal.tostring())
        length = len(val1.fft_fs)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.fft_fs.tostring())
        length = len(val1.fft)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.fft.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.variance_map is None:
        self.variance_map = sensor_msgs.msg.CompressedImage()
      if self.candidates is None:
        self.candidates = None
      if self.led_all_unfiltered is None:
        self.led_all_unfiltered = duckietown_msgs.msg.LEDDetectionArray()
      end = 0
      _x = self
      start = end
      end += 5
      (_x.state, _x.capture_progress,) = _get_struct_Bf().unpack(str[start:end])
      start = end
      end += 8
      self.cell_size = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=2)
      start = end
      end += 16
      self.crop_rect_norm = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      _x = self
      start = end
      end += 12
      (_x.variance_map.header.seq, _x.variance_map.header.stamp.secs, _x.variance_map.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.variance_map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.variance_map.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.variance_map.format = str[start:end].decode('utf-8')
      else:
        self.variance_map.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.variance_map.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.candidates = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.Vector2D()
        _x = val1
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        self.candidates.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.led_all_unfiltered.detections = []
      for i in range(0, length):
        val1 = duckietown_msgs.msg.LEDDetection()
        _v10 = val1.timestamp1
        _x = _v10
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v11 = val1.timestamp2
        _x = _v11
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v12 = val1.pixels_normalized
        _x = _v12
        start = end
        end += 8
        (_x.x, _x.y,) = _get_struct_2f().unpack(str[start:end])
        start = end
        end += 4
        (val1.frequency,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.color = str[start:end].decode('utf-8')
        else:
          val1.color = str[start:end]
        start = end
        end += 4
        (val1.confidence,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.signal_ts = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.signal = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.fft_fs = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.fft = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.led_all_unfiltered.detections.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Bf = None
def _get_struct_Bf():
    global _struct_Bf
    if _struct_Bf is None:
        _struct_Bf = struct.Struct("<Bf")
    return _struct_Bf
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I