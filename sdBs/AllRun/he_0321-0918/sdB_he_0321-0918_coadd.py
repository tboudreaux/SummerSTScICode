from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[50.941042,-9.137667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0321-0918/sdB_he_0321-0918_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0321-0918/sdB_he_0321-0918_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
