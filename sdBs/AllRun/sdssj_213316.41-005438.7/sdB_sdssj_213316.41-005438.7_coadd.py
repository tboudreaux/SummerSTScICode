from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[323.318375,0.91075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_213316.41-005438.7/sdB_sdssj_213316.41-005438.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_213316.41-005438.7/sdB_sdssj_213316.41-005438.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()