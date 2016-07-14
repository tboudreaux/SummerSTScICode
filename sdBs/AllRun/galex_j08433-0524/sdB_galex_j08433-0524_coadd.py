from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[130.82875,-5.407642],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j08433-0524/sdB_galex_j08433-0524_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j08433-0524/sdB_galex_j08433-0524_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
