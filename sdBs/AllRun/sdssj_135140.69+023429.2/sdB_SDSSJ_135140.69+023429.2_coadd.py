from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[207.919542,2.574778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_135140.69+023429.2/sdB_SDSSJ_135140.69+023429.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_135140.69+023429.2/sdB_SDSSJ_135140.69+023429.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
