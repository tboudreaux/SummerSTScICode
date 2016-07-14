from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[338.841542,-50.355456],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j223521.97-502119.64/sdB_galex_j223521.97-502119.64_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j223521.97-502119.64/sdB_galex_j223521.97-502119.64_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
