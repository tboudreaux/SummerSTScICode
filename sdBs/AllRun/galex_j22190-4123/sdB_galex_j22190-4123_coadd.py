from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[334.756792,-41.392175],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j22190-4123/sdB_galex_j22190-4123_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j22190-4123/sdB_galex_j22190-4123_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
