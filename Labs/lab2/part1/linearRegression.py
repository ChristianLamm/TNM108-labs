import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


sns.set()


class GaussianFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced Gaussian features for one-dimensional input."""

    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor
        self.centers_ = None
        self.width_ = None

    @staticmethod
    def _gauss_basis(X_arr, centers, width, axis=None):
        arg = (X_arr - centers) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis=axis))

    def fit(self, X_in, y=None):
        del y
        self.centers_ = np.linspace(X_in.min(), X_in.max(), self.N)
        if self.N > 1:
            self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        else:
            self.width_ = 1.0
        return self

    def transform(self, X_in):
        return self._gauss_basis(X_in[:, :, np.newaxis], self.centers_, self.width_, axis=1)


def main() -> None:
    """Demo: simple linear, multivariate, polynomial and Gaussian-basis fits."""
    rng = np.random.default_rng(1)  # pylint: disable=no-member

    x = 10 * rng.random(50)
    y = 2 * x - 5 + rng.standard_normal(50)

    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)

    xfit = np.linspace(0, 10, 1000)
    yfit = model.predict(xfit[:, np.newaxis])

    print("Model slope:", model.coef_[0])
    print("Model intercept:", model.intercept_)

    # polynomial example (quick)
    poly_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
    poly_model.fit(x[:, np.newaxis], np.sin(x))

    gauss_model = make_pipeline(GaussianFeatures(10), LinearRegression())
    gauss_model.fit(x[:, np.newaxis], np.sin(x))

    # plotting (optional)
    plt.scatter(x, y, label="data")
    plt.plot(xfit, yfit, color="red", label="linear fit")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

sns.set()


# GAUSSIAN BASIS FUNCTIONS

class GaussianFeatures(BaseEstimator, TransformerMixin):
   """Uniformly spaced Gaussian features for one-dimensional input."""

   def __init__(self, N, width_factor=2.0):
      self.N = N
      self.width_factor = width_factor
      # initialize attributes set in fit to satisfy linters
      self.centers_ = None
      self.width_ = None

   @staticmethod
   def _gauss_basis(X_arr, centers, width, axis=None):
      arg = (X_arr - centers) / width
      return np.exp(-0.5 * np.sum(arg ** 2, axis=axis))

   def fit(self, X_in, y=None):
      # create N centers spread along the data range
      del y
      self.centers_ = np.linspace(X_in.min(), X_in.max(), self.N)
      if self.N > 1:
         self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
      else:
         self.width_ = 1.0
      return self

   def transform(self, X_in):
      return self._gauss_basis(X_in[:, :, np.newaxis], self.centers_, self.width_, axis=1)


def main() -> None:
   """Demo: simple linear, multivariate, polynomial and Gaussian-basis fits.

   All plotting and example data live inside main so importing this module
   doesn't execute the demo (helps linters and tests).
   """
   # use Generator API (avoids Pylint no-member on RandomState)
   rng = np.random.default_rng(1)  # pylint: disable=no-member

   x = 10 * rng.random(50)
   y = 2 * x - 5 + rng.standard_normal(50)
   plt.scatter(x, y)
   plt.show()

   model = LinearRegression(fit_intercept=True)
   model.fit(x[:, np.newaxis], y)
   xfit = np.linspace(0, 10, 1000)
   yfit = model.predict(xfit[:, np.newaxis])
   plt.scatter(x, y)
   plt.plot(xfit, yfit)
   plt.show()

   print("Model slope: ", model.coef_[0])
   print("Model intercept:", model.intercept_)

   X = 10 * rng.random((100, 3))
   y = 0.5 + np.dot(X, [1.5, -2.0, 1.0])
   model.fit(X, y)
   print(model.intercept_)
   print(model.coef_)

   # POLYNOMIAL BASIS FUNCTIONS
   x = np.array([2, 3, 4])
   poly = PolynomialFeatures(3, include_bias=False)
   poly.fit_transform(x[:, None])

   poly_model = make_pipeline(PolynomialFeatures(7), LinearRegression())

   x = 10 * rng.random(50)
   y = np.sin(x) + 0.1 * rng.standard_normal(50)
   xfit = np.linspace(0, 10, 1000)
   poly_model.fit(x[:, np.newaxis], y)
   yfit = poly_model.predict(xfit[:, np.newaxis])
   plt.scatter(x, y)
   plt.plot(xfit, yfit)
   plt.show()

   gauss_model = make_pipeline(GaussianFeatures(20), LinearRegression())
   gauss_model.fit(x[:, np.newaxis], y)
   yfit = gauss_model.predict(xfit[:, np.newaxis])

   plt.scatter(x, y)
   plt.plot(xfit, yfit)
   plt.xlim(0, 10)
   plt.show()


if __name__ == "__main__":
   main()

