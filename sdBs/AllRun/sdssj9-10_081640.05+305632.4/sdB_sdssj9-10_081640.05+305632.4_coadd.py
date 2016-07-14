from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[124.166875,30.942333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_081640.05+305632.4/sdB_sdssj9-10_081640.05+305632.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_081640.05+305632.4/sdB_sdssj9-10_081640.05+305632.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
