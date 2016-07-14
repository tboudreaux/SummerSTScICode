from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[120.59325,18.952194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_080222.38+185707.9/sdB_SDSSJ_080222.38+185707.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_080222.38+185707.9/sdB_SDSSJ_080222.38+185707.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
