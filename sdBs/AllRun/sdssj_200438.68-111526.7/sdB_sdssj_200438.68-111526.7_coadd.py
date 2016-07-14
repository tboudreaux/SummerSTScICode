from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[301.161167,-11.257417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_200438.68-111526.7/sdB_sdssj_200438.68-111526.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_200438.68-111526.7/sdB_sdssj_200438.68-111526.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
