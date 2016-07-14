from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[85.277833,-42.758858],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_0539-4246/sdB_HE_0539-4246_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_0539-4246/sdB_HE_0539-4246_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
