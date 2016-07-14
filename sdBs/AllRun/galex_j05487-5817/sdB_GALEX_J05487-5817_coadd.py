from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[87.189,-58.289797],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J05487-5817/sdB_GALEX_J05487-5817_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J05487-5817/sdB_GALEX_J05487-5817_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
