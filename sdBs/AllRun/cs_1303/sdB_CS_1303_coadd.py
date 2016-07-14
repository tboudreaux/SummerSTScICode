from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[196.539542,-62.642778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CS_1303/sdB_CS_1303_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CS_1303/sdB_CS_1303_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
