from django.test import TestCase 
import importlib 
import inspect 
import uuid
from unittest.mock import Mock 

class TestUtilFunctions(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_its_running(self) -> None:
    self.assertTrue(True)
    
  def test_if_can_import_util_module(self) -> None:
    try:
      import users.utils as utils
      self.assertIsNotNone(utils)
    except ImportError:
      self.fail("Was not possible to import the util module")
      
  def test_if_utils_module_have_validate_uuid_function(self) -> None:  
    module = importlib.import_module("users.utils")
    self.assertTrue(hasattr(module, "validate_uuid_param"))
    
  def test_if_utils_module_validate_function_have_correct_signature(self) -> None:
    module = importlib.import_module("users.utils")
    signature = inspect.signature(module.validate_uuid_param)
    params = list(signature.parameters.keys())
    self.assertEqual(params[0], "view")
    
  def test_if_utils_module_validate_uuid_function_works_correctly(self) -> None:
    from users.utils import validate_uuid_param
    mock_view = Mock(return_value="success")
    decorated_view = validate_uuid_param(mock_view)
    request = Mock()
    valid_uuid = "12345678-1234-5678-9012-123456789012"
    result = decorated_view(None, request, valid_uuid)
    self.assertEqual(result, "success")
    mock_view.assert_called_once_with(None, request, uuid.UUID(valid_uuid))
    
    # Test with invalid UUID
    mock_view.reset_mock()
    invalid_uuid = "invalid-uuid"
    response = decorated_view(None, request, invalid_uuid)
    self.assertEqual(response.status_code, 400)
    self.assertIn("error", response.data)
    mock_view.assert_not_called()
    
    # Test with valid UUID and extra args
    mock_view.reset_mock()
    mock_view.return_value = "success_with_args"
    result = decorated_view(None, request, valid_uuid, "extra_arg", kwarg="value")
    self.assertEqual(result, "success_with_args")
    mock_view.assert_called_once_with(None, request, uuid.UUID(valid_uuid), "extra_arg", kwarg="value")
    