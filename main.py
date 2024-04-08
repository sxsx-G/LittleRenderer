import math

from Definition import *

MY_PI = 3.14159265358979323846
MY_PI_OVER_180 = MY_PI / 180.0


def get_view_matrix(eye_pos: Vector3f) -> Matrix4f:
    view = np.eye(4)

    translate = np.eye(4)
    translate[:3, 3] = -eye_pos

    view = np.dot(translate, view)

    return view


def get_rotation_matrix(axis: Vector3f, angle: float) -> Matrix3f:
    angle = np.radians(angle)
    axis = axis / np.linalg.norm(axis)

    a = math.cos(angle / 2.0)
    b, c, d = -axis * math.sin(angle / 2.0)

    return np.array([[a * a + b * b - c * c - d * d, 2 * (b * c - a * d), 2 * (b * d + a * c)],
                     [2 * (b * c + a * d), a * a + c * c - b * b - d * d, 2 * (c * d - a * b)],
                     [2 * (b * d - a * c), 2 * (c * d + a * b), a * a + d * d - b * b - c * c]])


def get_model_matrix(translation: Vector3f, axis: Vector3f, angle: float, scale: Vector3f) -> Matrix4f:
    model = np.eye(4)

    translate = np.eye(4)
    translate[:3, 3] = translation

    rotate = np.eye(4)
    rotate[:3, :3] = get_rotation_matrix(axis, angle)

    scale_matrix = np.eye(4)
    scale_matrix[0, 0] = scale[0]
    scale_matrix[1, 1] = scale[1]
    scale_matrix[2, 2] = scale[2]

    model = np.dot(scale_matrix, model)
    model = np.dot(rotate, model)
    model = np.dot(translate, model)

    return model


def get_projection_matrix(fov: float, aspect: float, near: float, far: float) -> Matrix4f:
    projection = np.eye(4)

    tan_half_fov = math.tan(fov * MY_PI / 360.0)
    t = near * tan_half_fov
    r = aspect * t
    left = -r
    b = -t

    projection[0, 0] = 2 * near / (r - left)
    projection[0, 2] = (r + left) / (r - left)
    projection[1, 1] = 2 * near / (t - b)
    projection[1, 2] = (t + b) / (t - b)
    projection[2, 2] = -(far + near) / (far - near)
    projection[2, 3] = -2 * far * near / (far - near)
    projection[3, 2] = -1
    projection[3, 3] = 0

    return projection


if __name__ == '__main__':
    print('PyCharm')
