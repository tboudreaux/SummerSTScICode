from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[46.533125,38.39325],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_030607.95+382335.7/sdB_SDSSJ_030607.95+382335.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_030607.95+382335.7/sdB_SDSSJ_030607.95+382335.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
