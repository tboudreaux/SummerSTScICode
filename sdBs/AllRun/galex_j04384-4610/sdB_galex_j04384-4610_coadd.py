from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[69.613,-46.181478],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j04384-4610/sdB_galex_j04384-4610_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j04384-4610/sdB_galex_j04384-4610_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
