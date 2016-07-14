from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[161.583958,10.274917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_104620.15+101629.7/sdB_SDSSJ_104620.15+101629.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_104620.15+101629.7/sdB_SDSSJ_104620.15+101629.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
