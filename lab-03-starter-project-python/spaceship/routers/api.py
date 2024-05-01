from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/multiplied_matrix')
def get_multiplied_matrix() -> dict:
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    multiplied_matrix = numpy.dot(matrix_a, matrix_b)
    final_result = {
        "maxtrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "final_result": multiplied_matrix.tolist()
    }
    return final_result



