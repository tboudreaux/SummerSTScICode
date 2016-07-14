from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[107.546167,40.605842],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j07101+4036/sdB_galex_j07101+4036_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j07101+4036/sdB_galex_j07101+4036_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
