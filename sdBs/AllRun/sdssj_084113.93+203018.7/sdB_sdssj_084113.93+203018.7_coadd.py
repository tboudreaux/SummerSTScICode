from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[130.308042,20.505194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_084113.93+203018.7/sdB_sdssj_084113.93+203018.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_084113.93+203018.7/sdB_sdssj_084113.93+203018.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
